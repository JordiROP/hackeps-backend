from fastapi import APIRouter
from .modules.association.routes.router import asso_router
api_router = APIRouter()

api_router.include_router(asso_router, tags=['association'], prefix='/asso')
