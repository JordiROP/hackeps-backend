from fastapi import FastAPI

from .core.config import load_env 
from .router import api_router

def get_app() -> FastAPI:
    app = FastAPI(
        title='LleidaHack -- General Application Backend',
        version='0.0.1',
        debug=True,
    )
    app.include_router(api_router)
    return app

load_env()
app = get_app()