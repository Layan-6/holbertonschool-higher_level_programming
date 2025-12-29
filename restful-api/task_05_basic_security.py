#!/usr/bin/env python3
"""
Task 5: API Security and Authentication
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Basic Auth
@auth.verify_password
def verify_password(username, password):
    if username in users:
        if check_password_hash(users[username]['password'], password):
            return username
    return None

@auth.error_handler
def auth_error():
    return "Unauthorized", 401

# JWT Error Handlers
@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(callback):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_callback(callback):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def revoked_token_callback(callback):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(callback):
    return jsonify({"error": "Fresh token required"}), 401

# Routes
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask API"})

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    # PLAIN TEXT, not JSON
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    
    if username in users:
        if check_password_hash(users[username]['password'], password):
            claims = {"role": users[username]['role']}
            token = create_access_token(identity=username, additional_claims=claims)
            return jsonify({"access_token": token})
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    # PLAIN TEXT, not JSON
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    # PLAIN TEXT, not JSON
    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run(debug=False, port=5000)
