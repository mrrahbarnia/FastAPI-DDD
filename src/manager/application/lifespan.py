import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from src.infrastructure.bootstrap import bootstrap

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_application: FastAPI) -> AsyncGenerator:
    # ============================== On startup
    logger.info("Application is running...")

    logger.info("Bootstraping...")
    bootstrap()

    yield
    # ============================== On shutdown

    logger.info("Application is shutting down...")
