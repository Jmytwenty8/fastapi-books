from fastapi import APIRouter, status, Depends
from models.books_schema import Book, BookUpdate
from models.response_schema import ResponseModel, APIError
from services.book_service import BookService

book_router = APIRouter()


@book_router.get("/", response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def get_books(book_service: BookService = Depends()) -> ResponseModel:
    books = book_service.get_books()
    return ResponseModel(
        status="success",
        data={"books": books},
        message="Books retrieved successfully",
    )


@book_router.post(
    "/", response_model=ResponseModel, status_code=status.HTTP_201_CREATED
)
async def add_book(book: Book, book_service: BookService = Depends()) -> ResponseModel:
    new_book = book_service.add_book(book)
    return ResponseModel(
        status="success", data={"book": new_book}, message="Book added successfully"
    )


@book_router.get(
    "/{book_id}", response_model=ResponseModel, status_code=status.HTTP_200_OK
)
async def get_book(
    book_id: int, book_service: BookService = Depends()
) -> ResponseModel:
    book = book_service.get_book(book_id)
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
    book_id: int, book: BookUpdate, book_service: BookService = Depends()
) -> ResponseModel:
    updated_book = book_service.update_book(book_id, book)
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
async def delete_book(
    book_id: int, book_service: BookService = Depends()
) -> ResponseModel:
    success = book_service.delete_book(book_id)
    if success:
        return ResponseModel(status="success", message="Book deleted successfully")
    raise APIError(message="Book not found", status_code=status.HTTP_404_NOT_FOUND)
