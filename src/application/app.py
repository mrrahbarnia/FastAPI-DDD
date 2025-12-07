from fastapi import FastAPI

from src.common.types import Environment
from src.config.general import General
from src.config.fastapi import FastAPI as fastapi_config

fastapi_cfg = fastapi_config()  # type: ignore
general_cfg = General()  # type: ignore


app: FastAPI = FastAPI(
    title=fastapi_cfg.APPLICATION_NAME,
    description=fastapi_cfg.APPLICATION_DESCRIPTION,
    version=fastapi_cfg.APPLICATION_VERSION,
    docs_url=None
    if general_cfg.ENVIRONMENT == Environment.PRODUCTION
    else fastapi_cfg.DOCS_URL,
    openapi_url=None
    if general_cfg.ENVIRONMENT == Environment.PRODUCTION
    else fastapi_cfg.OPENAPI_URL,
    redoc_url=None
    if general_cfg.ENVIRONMENT == Environment.PRODUCTION
    else fastapi_cfg.REDOC_URL,
)
