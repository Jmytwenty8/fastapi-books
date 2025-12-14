from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from uuid import uuid4, UUID
from sqlalchemy.sql import func


class Book(SQLModel, table=True):
    id: UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid4)
    )
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, server_default=func.now())
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now()
        )
    )

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author})>"


class BookCreateModel(SQLModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
