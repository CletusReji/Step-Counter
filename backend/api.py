from flask import Flask, request, jsonify
from firebase_config import db

app = Flask(__name__)

# Add Step Data for User
@app.route("/add_step", methods=["POST"])
def add_step():
    data = request.json
    username = data.get("username")
    date = data.get("date")
    steps = data.get("steps")

    user_ref = db.collection("users").document(username)
    if not user_ref.get().exists:
        return jsonify({"error": "User not found"}), 404

    steps_ref = user_ref.collection("steps").document(date)
    steps_ref.set({"date": date, "steps": steps})

    return jsonify({"message": "Step record added!"}), 201

# Retrieve User Step Data
@app.route("/get_steps/<username>", methods=["GET"])
def get_steps(username):
    user_ref = db.collection("users").document(username)
    if not user_ref.get().exists:
        return jsonify({"error": "User not found"}), 404

    steps_ref = user_ref.collection("steps").stream()
    step_data = [{"date": doc.id, "steps": doc.to_dict()["steps"]} for doc in steps_ref]

    return jsonify(step_data), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)