import os
from typing import Union
from xmlrpc.client import boolean
from fastapi import APIRouter
from app.modules.base.repository import firebase_repository
from app.core.constants import DB_TYPE
from app.db.db_manager import DBManager
from app.modules.tournament.models import User
from app.modules.tournament.errors import Error
tournament_router = APIRouter()

@tournament_router.get('/users/{id}')
async def get_user_by_id(id:str) -> Union[User, Error]:
    dbManager = DBManager(os.getenv(DB_TYPE))
    return firebase_repository.get_user_by_id(dbManager.db, id)

@tournament_router.put('/users/{id}')
async def upsert_user(id: str, user: User) -> Union[str, Error]:
    dbManager = DBManager(os.getenv(DB_TYPE))
    return firebase_repository.upsert_user(dbManager.db, id, user)

@tournament_router.post('/users/{id}')
async def enable_user(id: str) -> Union[str, Error]:
    dbManager = DBManager(os.getenv(DB_TYPE))
    return firebase_repository.enable_userby_id(dbManager.db, id)

@tournament_router.delete('/users/{id}')
async def disable_user(id:str) -> Union[bool, Error]:
    dbManager = DBManager(os.getenv(DB_TYPE))
    return firebase_repository.disable_userby_id(dbManager.db, id)
