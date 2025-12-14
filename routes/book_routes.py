from fastapi import APIRouter, status, Depends
from models.books_schema import BookUpdate, BookCreateModel
from models.response_schema import ResponseModel, APIError
from services.book_service import BookService
from db import get_session

book_router = APIRouter()


@book_router.get("/", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def get_books(session=Depends(get_session)) -> ResponseModel:
    book_service = BookService()
    books = await book_service.get_books(session)
    return ResponseModel(
        status="success",
        data={"books": books},
        message="Books retrieved successfully",
    )


@book_router.post(
    "/", response_model=ResponseModel, status_code=status.HTTP_201_CREATED
)
async def add_book(
    book: BookCreateModel, session=Depends(get_session)
) -> ResponseModel:
    book_service = BookService()
    new_book = await book_service.add_book(book, session)
    return ResponseModel(
        status="success", data={"book": new_book}, message="Book added successfully"
    )


@book_router.get(
    "/{book_id}", response_model=ResponseModel, status_code=status.HTTP_200_OK
)
async def get_book(book_id: str, session=Depends(get_session)) -> ResponseModel:
    book_service = BookService()
    book = await book_service.get_book(book_id, session)
    if book:
        return ResponseModel(
            status="success",
            data={"book": book},
            message="Book retrieved successfully",
        )
    raise APIError(message="Book not found", status_code=status.HTTP_404_NOT_FOUND)


@book_router.patch(
    "/{book_id}", response_model=ResponseModel, status_code=status.HTTP_200_OK
)
async def update_book(
    book_id: str, book: BookUpdate, session=Depends(get_session)
) -> ResponseModel:
    book_service = BookService()
    updated_book = await book_service.update_book(book_id, book, session)
    if updated_book:
        return ResponseModel(
            status="success",
            data={"book": updated_book},
            message="Book updated successfully",
        )
    raise APIError(message="Book not found", status_code=status.HTTP_404_NOT_FOUND)


@book_router.delete(
    "/{book_id}", response_model=ResponseModel, status_code=status.HTTP_200_OK
)
async def delete_book(book_id: str, session=Depends(get_session)) -> ResponseModel:
    book_service = BookService()
    success = await book_service.delete_book(book_id, session)
    if success:
        return ResponseModel(status="success", message="Book deleted successfully")
    raise APIError(message="Book not found", status_code=status.HTTP_404_NOT_FOUND)
