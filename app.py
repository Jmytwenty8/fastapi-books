from fastapi import (
    FastAPI,
)
from models.response_schema import APIError
from routes import router
from utils.exception_handler import api_error_handler
from contextlib import asynccontextmanager
from db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    await init_db()
    yield
    # Shutdown actions


version = "v1"

app = FastAPI(version=version, lifespan=lifespan)

app.add_exception_handler(APIError, api_error_handler)
app.include_router(router, prefix=f"/api/{version}")
