#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt_claims
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'  # Set a secret key for JWT token generation
jwt = JWTManager(app)
basic_auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("admin_password"), "role": "admin"}
}

@basic_auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username).get('password'), password):
        return username
    return None

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and check_password_hash(users.get(username).get('password'), password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid username or password"}), 401


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return users.get(identity)


@jwt_required()
@app.route('/jwt-protected', methods=['GET'])
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"})

@jwt_required()
@app.route('/admin-only', methods=['GET'])
def admin_only():
    current_user_role = get_jwt_claims().get('role')
    if current_user_role == 'admin':
        return jsonify({"message": "Admin Access: Granted"})
    else:
        return jsonify({"error": "Unauthorized access"}), 403
@jwt.unauthorized_loader
def unauthorized_handler(callback):
    return jsonify({"error": "Missing Authorization Header"}), 401

@jwt.invalid_token_loader
def invalid_token_handler(callback):
    return jsonify({"error": "Invalid JWT token"}), 401

@jwt.expired_token_loader
def expired_token_handler(callback):
    return jsonify({"error": "Expired JWT token"}), 401

@jwt.revoked_token_loader
def revoked_token_handler(callback):
    return jsonify({"error": "Revoked JWT token"}), 401

if __name__ == "__main__":
    app.run()