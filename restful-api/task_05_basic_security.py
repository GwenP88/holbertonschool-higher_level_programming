#!/usr/bin/python3
"""Flask API with Basic Auth and JWT (role-based access control)."""

# ----- Imports -----
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager
)

# ----- App & Auth setup -----
app = Flask(__name__)
auth = HTTPBasicAuth()

# ----- In-memory users (hashed passwords + roles) -----
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


# ----- Basic Authentication (HTTPBasicAuth) -----
@auth.verify_password
def verify_user(username, password):
    """Verify Basic Auth credentials against in-memory users."""
    if (
        username in users
        and check_password_hash(users[username]["password"], password)
    ):
        return username
    return None


# ----- Basic Auth routes -----
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Basic-auth protected endpoint."""
    return "Basic Auth: Access Granted"


# ----- JWT setup -----
app.config["JWT_SECRET_KEY"] = "secret_key"
jwt = JWTManager(app)


# ----- JWT error handlers (always return 401) -----
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Return 401 for missing/unauthorized JWT access."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Return 401 for invalid or malformed JWTs."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Return 401 for expired JWTs."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Return 401 for revoked JWTs."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Return 401 when a fresh JWT is required."""
    return jsonify({"error": "Fresh token required"}), 401


# ----- JWT login route -----
@app.route("/login", methods=["POST"])
def login():
    """Authenticate user credentials and issue a JWT access token."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 401
    else:
        username = data.get("username", None)
        password = data.get("password", None)

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)
    if user is None or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token})


# ----- JWT protected routes -----
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def protected():
    """JWT-protected endpoint."""
    return jsonify({"message": "JWT Auth: Access Granted"})


# ----- Role-based access control routes -----
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """JWT-protected admin-only endpoint (role check)."""
    identity = get_jwt_identity()
    user_role = users[identity]["role"]
    if user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


if __name__ == "__main__":
    app.run()
