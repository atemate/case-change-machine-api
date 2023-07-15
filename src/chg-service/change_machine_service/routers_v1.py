import json

from fastapi import APIRouter
from src.models.book_models_v1 import Book

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id):
    books = []
    with open("books_v1.json", "r") as file:
        books = json.load(file)

    return Book.parse_obj(books[book_id])
