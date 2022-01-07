from app.core.config.db_types import FIREBASE_DB
from app.core.persistance.firebase import FirestoreManager


class DBManager:
    @classmethod
    def create_db_instance(cls, db_type:str):
        if db_type == FIREBASE_DB:
            return FirestoreManager()
        else:
            raise Exception
