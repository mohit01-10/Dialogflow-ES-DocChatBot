from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_auth
import dialogflow
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./config/service-account.json"


app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    session_id = data.get('session_id', 'default_session')
    message = data.get('message')

    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400

    response = dialogflow.detect_intent(session_id, message)
    return jsonify({"response": response})


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = firebase_auth.register_user(email, password)

    if "uid" in user:
        return jsonify({"message": "Registration successful", "uid": user["uid"]})
    else:
        return jsonify({"error": user["error"]}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = firebase_auth.login_user(email, password)

    if "uid" in user:
        return jsonify({"message": "Login successful", "uid": user["uid"], "token": user["idToken"]})
    else:
        return jsonify({"error": user["error"]}), 401

if __name__ == '__main__':
    app.run(debug=True)
