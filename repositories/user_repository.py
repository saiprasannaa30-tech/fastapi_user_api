from typing import Dict, Optional
from schemas.user import UserCreate

class UserRepository:
    def __init__(self):
        self.users: Dict[int, dict] = {}
        self.user_id_counter = 1

    def create(self, user: UserCreate) -> dict:
        new_user = {
            "id": self.user_id_counter,
            "name": user.name,
            "age": user.age
        }
        self.users[self.user_id_counter] = new_user
        self.user_id_counter += 1
        return new_user

    def get_all(self):
        return list(self.users.values())

    def get_by_id(self, user_id: int) -> Optional[dict]:
        return self.users.get(user_id)

    def delete(self, user_id: int) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
