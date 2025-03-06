from flask import Flask, jsonify
from database import get_step_records

app = Flask(__name__)

@app.route("/get_data", methods=["GET"])
def get_data():
    step_data = get_step_records()
    return jsonify(step_data)

if __name__ == "__main__":
    app.run(debug=True)