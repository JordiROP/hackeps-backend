import firebase_admin
import os
import base64
import json
from firebase_admin import credentials
from firebase_admin import firestore

from ..config.env_var import FIREBASE_KEY

class FirestoreManager:
    db = None
    def __init__(self):
        if self.db is None:
            encoded_firebase_key = os.environ[FIREBASE_KEY]
            firebase_key = base64.b64decode(encoded_firebase_key).decode('UTF-8')
            cred = credentials.Certificate(json.loads(firebase_key))
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()


        