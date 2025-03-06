import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials
cred = credentials.Certificate("backend/firebase_credentials.json")
firebase_admin.initialize_app(cred)

# Get Firestore database reference
db = firestore.client()