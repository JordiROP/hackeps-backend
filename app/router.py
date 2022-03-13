from fastapi import APIRouter
from app.modules.tournament import router
api_router = APIRouter()

api_router.include_router(router.tournament_router, tags=['tournament'], prefix='/tournament')
