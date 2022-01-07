from fastapi.routing import APIRouter

members_router = APIRouter()
@members_router.get('/users')
async def get_users():
    return {'msg': 'method not implemented yet', 'code': 500}