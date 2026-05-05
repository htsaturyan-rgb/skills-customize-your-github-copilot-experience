# Starter Code for Persistent CRUD API with FastAPI and SQLite

import sqlite3
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB_FILE = "books.db"

app = FastAPI(title="FastAPI SQLite CRUD")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/books")
def list_books() -> list[dict[str, Any]]:
    conn = get_connection()
    rows = conn.execute("SELECT id, title, author, year FROM books ORDER BY id").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/books/{book_id}")
def get_book(book_id: int) -> dict[str, Any]:
    conn = get_connection()
    row = conn.execute(
        "SELECT id, title, author, year FROM books WHERE id = ?",
        (book_id,),
    ).fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return dict(row)


# TODO: Implement POST /books
# - Validate request body with BookInput
# - Insert into SQLite
# - Return created book with generated id


# TODO: Implement PUT /books/{book_id}
# - Check if the book exists
# - Update title, author, and year
# - Return updated book or 404 when missing


# TODO: Implement DELETE /books/{book_id}
# - Check if the book exists
# - Delete the row
# - Return a success message or 404 when missing


# Run locally with:
# uvicorn starter-code:app --reload
