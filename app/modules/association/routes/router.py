from fastapi.routing import APIRouter
from .members import members_router

asso_router = APIRouter()

asso_router.include_router(members_router, prefix='/user')