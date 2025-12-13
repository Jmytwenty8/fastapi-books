from typing import List, Optional, Dict, Any
from models.books_schema import Book, BookUpdate
from db import books_db


class BookService:
    def get_books(self) -> List[Dict[str, Any]]:
        return books_db

    def get_book(self, book_id: int) -> Optional[Dict[str, Any]]:
        for book in books_db:
            if book["id"] == book_id:
                return book
        return None

    def add_book(self, book: Book) -> Dict[str, Any]:
        new_book = book.model_dump()
        books_db.append(new_book)
        return new_book

    def update_book(
        self, book_id: int, book_update: BookUpdate
    ) -> Optional[Dict[str, Any]]:
        for index, existing_book in enumerate(books_db):
            if existing_book["id"] == book_id:
                update_data = book_update.model_dump(exclude_unset=True)
                books_db[index].update(update_data)
                return books_db[index]
        return None

    def delete_book(self, book_id: int) -> bool:
        for index, book in enumerate(books_db):
            if book["id"] == book_id:
                del books_db[index]
                return True
        return False
