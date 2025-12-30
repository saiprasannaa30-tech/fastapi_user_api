from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator
from typing import Dict

app = FastAPI()

users: Dict[int, dict] = {}
user_id_counter = 1

@app.middleware("http")
async def add_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-App-Name"] = "User API"
    return response

class UserCreate(BaseModel):
    name: str
    age: int

    @validator("name")
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v

    @validator("age")
    def validate_age(cls, v):
        if v <= 0:
            raise ValueError("Age must be greater than 0")
        return v

@app.get("/")
def home():
    return {"message": "FastAPI is running"}

@app.post("/users")
def create_user(user: UserCreate, request: Request):
    global user_id_counter
    new_user = {
        "id": user_id_counter,
        "name": user.name,
        "age": user.age
    }
    users[user_id_counter] = new_user
    user_id_counter += 1
    return JSONResponse(content=new_user)

@app.get("/users")
def get_users(limit: int | None = None):
    result = list(users.values())
    if limit:
        result = result[:limit]
    return JSONResponse(content=result)

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(content=users[user_id])

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted successfully"}
