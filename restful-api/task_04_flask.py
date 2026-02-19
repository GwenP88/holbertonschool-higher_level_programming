#!/usr/bin/python3
"""Simple Flask REST API for managing in-memory users."""
from flask import Flask, jsonify, request


users = {}
app = Flask(__name__)


@app.get("/")
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.get("/data")
def get_data():
    """Return the list of usernames as JSON."""
    return jsonify(list(users.keys()))


@app.get("/status")
def get_status():
    """Health-check endpoint returning OK."""
    return "OK"


@app.get("/users/<username>")
def get_user(username):
    """Return a user's data by username or 404 if not found."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.post("/add_user")
def add_user():
    """Create a new user from JSON payload with validation."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify(data), 201


if __name__ == "__main__":
    app.run()
