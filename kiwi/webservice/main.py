from fastapi import FastAPI
from .routes.router import api_router

def get_app() -> FastAPI:
    app = FastAPI(
        title='Kiwi - The HackEPS regulator',
        version='0.0.1',
        debug=True,
        root_path='/api',
        root_path_in_server=True
    )
    app.include_router(api_router)
    return app

app = get_app()
