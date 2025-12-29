#!/usr/bin/env python3
"""
Task 4: Flask API with user management
"""

from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# Start with EMPTY users dictionary as per requirements
users = {}

@app.route('/')
def home():
    """
    Root endpoint
    Returns: Welcome message
    """
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    """
    Get all usernames
    Returns: JSON list of usernames
    """
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status')
def get_status():
    """
    API status check
    Returns: "OK"
    """
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """
    Get user details by username
    
    Args:
        username: Username to lookup
        
    Returns:
        User object if found, error message if not
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user
    
    Expected JSON:
    {
        "username": "string",
        "name": "string",
        "age": number,
        "city": "string"
    }
    
    Returns:
        Success message with user data or error message
    """
    # Check if request contains JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    
    # Validate required fields
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    
    # Check for duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Create new user
    new_user = {
        "username": username,
        "name": data.get('name', ""),
        "age": data.get('age', 0),
        "city": data.get('city', "")
    }
    
    # Add to users dictionary
    users[username] = new_user
    
    # Return success response
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

if __name__ == '__main__':
    app.run(debug=False)  # Turn off debug for testing
