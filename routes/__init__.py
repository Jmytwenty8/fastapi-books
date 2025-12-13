from .book_routes import book_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(book_router, prefix="/books", tags=["Books"])
