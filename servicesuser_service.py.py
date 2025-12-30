from repositories.user_repository import UserRepository
from fastapi import HTTPException

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user):
        return self.repository.create(user)

    def get_users(self, limit: int | None = None):
        users = self.repository.get_all()
        return users[:limit] if limit else users

    def get_user(self, user_id: int):
        user = self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def delete_user(self, user_id: int):
        success = self.repository.delete(user_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
