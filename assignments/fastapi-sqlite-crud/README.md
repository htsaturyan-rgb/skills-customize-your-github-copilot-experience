# 📘 Assignment: Persistent CRUD API with FastAPI and SQLite

## 🎯 Objective

Build a database-backed REST API using FastAPI and SQLite so students can persist data, run SQL-style CRUD operations, and return proper HTTP responses.

## 📝 Tasks

### 🛠️ Set Up SQLite Persistence and Models

#### Description
Create a FastAPI project that stores book records in a local SQLite database instead of in-memory dictionaries.

#### Requirements
Completed program should:

- Create a SQLite database file (for example, `books.db`) on first run.
- Create a `books` table with fields: `id`, `title`, `author`, and `year`.
- Define a Pydantic model for request validation.
- Include a `GET /health` endpoint that returns a simple status JSON.


### 🛠️ Implement Full CRUD Endpoints

#### Description
Implement endpoints to create, read, update, and delete books using database queries.

#### Requirements
Completed program should:

- Implement `POST /books` to insert a new book and return the created record.
- Implement `GET /books` and `GET /books/{book_id}` to retrieve records.
- Implement `PUT /books/{book_id}` to update a book by ID.
- Implement `DELETE /books/{book_id}` to remove a book and return a success message.
- Return `404` with a clear error message when a record does not exist.
