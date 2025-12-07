from fastapi import APIRouter

from src.config.fastapi import FastAPI

router = APIRouter(prefix=f"{FastAPI.ENDPOINT_PREFIX}")

# ================ Including application routers here ================ #
