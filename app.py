from fastapi import (
    FastAPI,
)
from models.response_schema import APIError
from routes import router
from handlers.exception_handler import api_error_handler

app = FastAPI()

app.add_exception_handler(APIError, api_error_handler)
app.include_router(router)
