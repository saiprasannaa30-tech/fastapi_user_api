# FastAPI User Management API

This is a simple FastAPI application that manages users in memory (no database needed).

---

## Features

- Home route (`GET /`)
- Create users (`POST /users`)
- Get all users (`GET /users?limit=optional`)
- Get user by ID (`GET /users/{user_id}`)
- Delete user (`DELETE /users/{user_id}`)
- Middleware adds `X-App-Name: User API` header
- Pydantic validation for user name and age
- Swagger UI and ReDoc documentation

---

## Setup

1. Install dependencies
```bash
pip install fastapi uvicorn

3. Run the server
uvicorn main:app --reload

4. Open in browser

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

API Usage
Create User (POST /users)
{
  "name": "John",
  "age": 22
}

Get All Users (GET /users)
Optional query parameter:
/users?limit=2

Get User by ID (GET /users/1)
Delete User (DELETE /users/1)

Notes

Users are stored in memory (data resets when the server restarts)

No database is used

This project is created for learning FastAPI basics
