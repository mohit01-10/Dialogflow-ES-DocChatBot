import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("config/firebase-admin-sdk.json")
firebase_admin.initialize_app(cred)

def register_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return {"uid": user.uid}
    except Exception as e:
        return None

def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        return {"uid": user.uid}
    except Exception as e:
        return None
