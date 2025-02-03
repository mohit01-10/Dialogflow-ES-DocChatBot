# import firebase_admin
# from firebase_admin import credentials, auth

# cred = credentials.Certificate("config/firebase-admin-sdk.json")
# firebase_admin.initialize_app(cred)

# def register_user(email, password):
#     try:
#         user = auth.create_user(email=email, password=password)
#         return {"uid": user.uid}
#     except Exception as e:
#         return None

# def login_user(email, password):
#     try:
#         user = auth.get_user_by_email(email)
#         return {"uid": user.uid}
#     except Exception as e:
#         return None


# cred = credentials.Certificate("config/firebase-client.json")

# firebase_config = {
#     "apiKey": "AIzaSyD82aXjoO5K4cesQ2o6jH38tcUOAtMdaYo",
#     "authDomain": "documentchatbotv1.firebaseapp.com",
#     "databaseURL": "https://documentchatbotv1-default-rtdb.asia-southeast1.firebasedatabase.app",
#     "projectId": "documentchatbotv1",
#     "storageBucket": "documentchatbotv1.firebasestorage.app",
#     "messagingSenderId": "538226760356",
#     "appId": "1:538226760356:web:dcba8bc149bd08def4a431",
#     "measurementId": "G-7L4MEN20XT"
# }

import pyrebase
from firebase_admin import credentials
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch Firebase configuration from environment variables
firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID")
}


# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def register_user(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return {"uid": user["localId"]}
    except Exception as e:
        return {"error": str(e)}

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return {"uid": user["localId"], "idToken": user["idToken"]}
    except Exception as e:
        return {"error": str(e)}

    