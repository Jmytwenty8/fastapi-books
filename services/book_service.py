from typing import List, Optional, Dict, Any
from models.books_schema import Book, BookUpdate, BookCreateModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select


class BookService:
    async def get_books(self, session: AsyncSession) -> List[Dict[str, Any]]:
        statement = select(Book).order_by(Book.updated_at.desc())  # type: ignore
        result = await session.execute(statement)
        books = result.scalars().all()
        return [book.model_dump() for book in books]

    async def get_book(
        self, book_id: str, session: AsyncSession
    ) -> Optional[Dict[str, Any]]:
        statement = select(Book).where(Book.id == book_id)
        result = await session.execute(statement)
        book = result.scalar_one_or_none()
        if book:
            return book.model_dump()
        return None

    async def add_book(
        self, book: BookCreateModel, session: AsyncSession
    ) -> Dict[str, Any]:
        new_book = Book(**book.model_dump())
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book.model_dump()

    async def update_book(
        self, book_id: str, book_update: BookUpdate, session: AsyncSession
    ) -> Optional[Dict[str, Any]]:
        statement = select(Book).where(Book.id == book_id)
        result = await session.execute(statement)
        book = result.scalar_one_or_none()
        if not book:
            return None
        for key, value in book_update.model_dump(exclude_unset=True).items():
            setattr(book, key, value)  # Update the timestamp
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book.model_dump()

    async def delete_book(self, book_id: str, session: AsyncSession) -> bool:
        statement = select(Book).where(Book.id == book_id)
        result = await session.execute(statement)
        book = result.scalar_one_or_none()
        if not book:
            return False
        await session.delete(book)
        await session.commit()
        return True
