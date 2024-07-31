import firebase_admin
from firebase_admin import credentials, auth, firestore

# Path to your service account key file
if not firebase_admin._apps:
    cred = credentials.Certificate("/workspaces/Enterprise/consumerforensics.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()  # Initialize Firestore client
