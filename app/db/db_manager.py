import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from app.core.constants import FIREBASE_DB, FIREBASE_CONFIG

class FirestoreManager:
    db = None
    def __init__(self):
        if self.db is None:
            config = os.getenv(FIREBASE_CONFIG)
            json_conf = json.loads(config)
            cred = credentials.Certificate(json_conf)
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()

class DBManager:
    db = None
    def __init__(self, db_type:str):
        if DBManager.db == None:
            if db_type == FIREBASE_DB:
                DBManager.db = FirestoreManager().db
            else:
                print("DB TYPE {}".format(db_type))
