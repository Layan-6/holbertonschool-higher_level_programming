#!/usr/bin/env python3
"""
5. API Security and Authentication Techniques
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, verify_jwt_in_request, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['JWT_SECRET_KEY'] = 'super-secret-jwt-key-change-this-too'

# Initialize authentication modules
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User storage
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

# Basic authentication verification
@auth.verify_password
def verify_password(username, password):
    """Verify basic authentication credentials"""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@auth.error_handler
def auth_error():
    """Handle basic authentication errors"""
    return jsonify({"error": "Unauthorized"}), 401

# JWT error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing JWT token"""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token"""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired JWT token"""
    return jsonify({"error": "Token has expired"}), 401

# Routes
@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({"message": "Welcome to the Flask API Security Demo"})

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic authentication protected route"""
    return jsonify({"message": "Basic Auth: Access Granted"})

@app.route('/login', methods=['POST'])
def login():
    """JWT login endpoint"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    
    # Check credentials
    if username in users and check_password_hash(users[username]['password'], password):
        # Create access token with user identity and role
        additional_claims = {"role": users[username]['role']}
        access_token = create_access_token(
            identity=username,
            additional_claims=additional_claims
        )
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT protected route"""
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted"})

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin-only route (requires admin role)"""
    current_user = get_jwt_identity()
    
    # Get JWT claims to check role
    claims = get_jwt()
    user_role = claims.get('role', 'user')
    
    if user_role != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return jsonify({"message": "Admin Access: Granted"})

if __name__ == '__main__':
    app.run(debug=True)
