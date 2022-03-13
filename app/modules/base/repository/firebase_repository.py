from typing import Union
import os
from firebase_admin.firestore import _FirestoreClient
from app.modules.tournament.models import Status, User
from app.modules.tournament.errors import Error

def get_user_by_id(db:_FirestoreClient, id:str) -> Union[User, Error]:
    doc_ref = db.collection(u'testing_collection').document(os.getenv('ENVIRONMENT')).collection('users').document(id)
    doc = doc_ref.get()
    
    return User(**doc.to_dict())

def upsert_user(db:_FirestoreClient, id:str, user:User) -> Union[str, Error]:
    doc_ref = db.collection(u'testing_collection').document(os.getenv('ENVIRONMENT')).collection('users').document(id)
    doc_ref.set(user.dict())

    return user.id

def enable_userby_id(db:_FirestoreClient, id:str) -> Union[bool, Error]:
    doc_ref = db.collection(u'testing_collection').document(os.getenv('ENVIRONMENT')).collection('users').document(id)
    user_ref = doc_ref.get()
    if user_ref != None:
        user = User(**user_ref.to_dict())
        if user.status != Status.dropped:
            return False
        user.status = Status.waiting
        doc_ref = db.collection(u'testing_collection').document(os.getenv('ENVIRONMENT')).collection('users').document(id)
        doc_ref.set(user.dict())
        return True
    
    return False

def disable_userby_id(db:_FirestoreClient, id:str) -> Union[bool, Error]:
    doc_ref = db.collection(u'testing_collection').document(os.getenv('ENVIRONMENT')).collection('users').document(id)
    user_ref = doc_ref.get()
    if user_ref != None:
        user = User(**user_ref.to_dict())
        if user.status == Status.dropped:
            return False
        user.status = Status.dropped
        doc_ref = db.collection(u'testing_collection').document(os.getenv('ENVIRONMENT')).collection('users').document(id)
        doc_ref.set(user.dict())
        return True
    
    return False
