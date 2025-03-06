from flask import Flask, request, jsonify
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials

# Initialize Firebase Admin
if not firebase_admin._apps:
    cred = credentials.Certificate("backend/firebase_credentials.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
users_ref = db.collection("users")

app = Flask(__name__)

# Register User
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")  # Hash this in production!

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # Check if user already exists
    if users_ref.document(username).get().exists:
        return jsonify({"error": "User already exists"}), 409

    # Store user in Firebase
    users_ref.document(username).set({"password": password})
    return jsonify({"message": "User registered successfully!"}), 201

# Login User
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user_doc = users_ref.document(username).get()
    if not user_doc.exists or user_doc.to_dict()["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful!", "token": "fake_token"}), 200

if __name__ == "__main__":
    app.run(debug=True)
