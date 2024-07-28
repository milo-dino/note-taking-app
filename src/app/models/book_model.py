from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class Book(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(max_length=255)
    isbn: int = Field(default=1)