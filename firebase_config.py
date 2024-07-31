import firebase_admin
from firebase_admin import credentials, auth

# Check if the default app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('consumerforensics.json')
    firebase_admin.initialize_app(cred)
else:
    # If you need to initialize another app, provide a unique name
    cred = credentials.Certificate('consumerforensics.json')
    firebase_admin.initialize_app(cred, name='no_app_name')

# Example usage (optional, for testing purposes)
print("Firebase services initialized successfully.")
