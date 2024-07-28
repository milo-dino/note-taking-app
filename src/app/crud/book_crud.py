from typing import List
from uuid import UUID
from fastapi import HTTPException
from sqlmodel import Session, select
from models.book_model import Book

# Create
def create_book(*, session: Session, book_in: Book) -> Book:
    book = Book.model_validate(book_in)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

# Get All
def read_books(*, session: Session) -> List[Book]:
    return session.exec(select(Book)).all()

# Get One
def read_book(*, session: Session, book_id: UUID) -> Book:
    db_book = session.get(Book, book_id)
    
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found.")
    
    return db_book