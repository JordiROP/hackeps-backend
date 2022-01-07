from fastapi import FastAPI

from .core.persistance.db_manager import DBManager
from .router import api_router
from .core.config.config import DB_TYPE

def get_app() -> FastAPI:
    app = FastAPI(
        title='LleidaHack -- General Application Backend',
        version='0.0.1',
        debug=True,
    )
    app.include_router(api_router)
    return app

db_manager = DBManager.create_db_instance(DB_TYPE)
app = get_app()