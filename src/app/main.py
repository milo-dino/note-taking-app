from typing import List
from uuid import UUID
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.templating import _TemplateResponse
from models.book_model import Book
from core.deps import SessionDep
from crud.book_crud import create_book, read_book, read_books

app = FastAPI()

templates = Jinja2Templates("../templates")

app.mount("/assets", StaticFiles(directory="../assets"), "asset")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse(request, "index.html")

@app.get("/goodbyeworld", response_class=HTMLResponse)
async def goodbyeworld(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse(request, "partials/goodbyeworld.html")

# Book endpoints

@app.post("/books", response_model=Book)
async def post_book(session: SessionDep, book_in: Book) -> Book:
    return create_book(session=session, book_in=book_in)

@app.get("/books", response_model=List[Book])
async def get_books(session: SessionDep) -> List[Book]:
    return read_books(session=session)

@app.get("/books/{book_id}", response_model=Book)
async def get_book(session: SessionDep, book_id: UUID) -> Book:
    return read_book(session=session, book_id=book_id)