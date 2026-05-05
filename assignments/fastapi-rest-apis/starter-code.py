# Starter Code for Building REST APIs with FastAPI Assignment

from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


# Simple in-memory store for this assignment.
books: Dict[int, BookInput] = {
    1: BookInput(title="Clean Code", author="Robert C. Martin", year=2008),
    2: BookInput(title="Fluent Python", author="Luciano Ramalho", year=2015),
}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]


# TODO: Implement POST /books
# Hint: assign a new ID as max existing key + 1.


# TODO: Implement PUT /books/{book_id}
# Hint: return 404 when the ID does not exist.


# TODO: Implement DELETE /books/{book_id}
# Hint: return a confirmation JSON after deletion.


# Run locally with:
# uvicorn starter-code:app --reload
