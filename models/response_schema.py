from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException


class ResponseModel(BaseModel):
    status: str
    data: Optional[dict] = None
    message: Optional[str] = None


class APIError(HTTPException):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=message)
