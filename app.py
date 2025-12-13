from fastapi import (
    FastAPI,
)
from models.response_schema import APIError
from routes import router
from utils.exception_handler import api_error_handler

version = "v1"

app = FastAPI(
    version=version,
)

app.add_exception_handler(APIError, api_error_handler)
app.include_router(router, prefix=f"/api/{version}")
