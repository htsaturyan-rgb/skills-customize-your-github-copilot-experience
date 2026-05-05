# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI to practice route creation, request validation, and proper HTTP responses for common CRUD operations.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI app and implement endpoints for managing a simple in-memory collection of books.

#### Requirements
Completed program should:

- Create a `GET /health` endpoint that returns a JSON status message.
- Create a `GET /books` endpoint that returns all books.
- Create a `GET /books/{book_id}` endpoint that returns one book by ID.
- Return `404` with a clear message when a book ID does not exist.


### 🛠️ Add Input Validation and CRUD Support

#### Description
Use Pydantic models to validate request data and finish the API with create, update, and delete behavior.

#### Requirements
Completed program should:

- Define a request model for creating and updating books (`title`, `author`, `year`).
- Create a `POST /books` endpoint to add a new book.
- Create a `PUT /books/{book_id}` endpoint to update an existing book.
- Create a `DELETE /books/{book_id}` endpoint to remove a book and return a success response.
