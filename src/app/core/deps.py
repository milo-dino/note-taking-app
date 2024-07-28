from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from collections.abc import Generator
from core.db import engine

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]