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
```  

### 2. Run the serverRun the server

```bash
uvicorn main:app --reload
```  

### 3. Open in browser
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Home route: http://127.0.0.1:8000/


