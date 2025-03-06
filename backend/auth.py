from flask import Flask, request, jsonify
from firebase_config import db
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Register User
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    users_ref = db.collection("users")
    user_doc = users_ref.document(username).get()

    if user_doc.exists:
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    users_ref.document(username).set({"username": username, "password": hashed_password})

    return jsonify({"message": "User registered successfully!"}), 201

# Login User
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    users_ref = db.collection("users")
    user_doc = users_ref.document(username).get()

    if not user_doc.exists:
        return jsonify({"error": "User not found"}), 404

    user_data = user_doc.to_dict()
    if not check_password_hash(user_data["password"], password):
        return jsonify({"error": "Invalid password"}), 401

    return jsonify({"message": "Login successful", "username": username}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)