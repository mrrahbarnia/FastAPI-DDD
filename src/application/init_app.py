from fastapi import FastAPI

from src.application import app
from src.application.exceptions import register_exception_handlers
from src.application.routers import router


def init_app() -> FastAPI:
    app.include_router(router)
    register_exception_handlers(app)
    return app


application: FastAPI = init_app()  # pass this to __main__.py or uvicorn command
