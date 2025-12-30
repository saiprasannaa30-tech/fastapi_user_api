from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    name: str
    age: int

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str):
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v

    @field_validator("age")
    @classmethod
    def validate_age(cls, v: int):
        if v <= 0:
            raise ValueError("Age must be greater than 0")
        return v


class UserResponse(BaseModel):
    id: int
    name: str
    age: int
