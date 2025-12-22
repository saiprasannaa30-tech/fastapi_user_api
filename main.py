from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, field_validator
from typing import Dict, Optional

# FastAPI app with explicit docs URLs
app = FastAPI(
    title="User API",
    docs_url="/docs",    # Swagger UI
    redoc_url="/redoc"   # Redoc
)

# In-memory storage for users
users: Dict[int, dict] = {}
user_id_counter = 1

# Middleware to add custom header
@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-App-Name"] = "User API"
    return response

# Pydantic v2 model for user creation with validation
class UserCreate(BaseModel):
    name: str
    age: int

    @field_validator("name")
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v

    @field_validator("age")
    def validate_age(cls, v):
        if v <= 0:
            raise ValueError("Age must be greater than 0")
        return v

# Home Route
@app.get("/")
def home():
    return {"message": "FastAPI is running"}

# Create User
@app.post("/users")
def create_user(user: UserCreate):
    global user_id_counter
    new_user = {
        "id": user_id_counter,
        "name": user.name,
        "age": user.age
    }
    users[user_id_counter] = new_user
    user_id_counter += 1
    return JSONResponse(content=new_user)

# Get All Users with optional limit
@app.get("/users")
def get_users(limit: Optional[int] = None):
    result = list(users.values())
    if limit:
        result = result[:limit]
    return JSONResponse(content=result)

# Get User by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(content=users[user_id])

# Delete User (Bonus)
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted successfully"}
