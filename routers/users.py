from fastapi import APIRouter, Query
from schemas.user import UserCreate, UserResponse
from services.user_service import UserService
from repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])

repository = UserRepository()
service = UserService(repository)

@router.post("", response_model=UserResponse)
def create_user(user: UserCreate):
    return service.create_user(user)

@router.get("", response_model=list[UserResponse])
def get_users(limit: int | None = Query(default=None)):
    return service.get_users(limit)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return service.get_user(user_id)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return service.delete_user(user_id)
