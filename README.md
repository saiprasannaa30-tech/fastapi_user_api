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

### 1. Install dependencies

```bash
pip install fastapi uvicorn
