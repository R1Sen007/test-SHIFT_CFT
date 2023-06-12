from typing import Union
from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    username: str 


class UserLogin(UserBase):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "ProUser007",
                "password": "Strong4Password!",
            }
        }


class UserCreate(UserLogin):
    email: Union[EmailStr, None] = None
    full_name: Union[str, None] = None

    class Config:
        schema_extra = {
            "example": {
                "username": "ProUser007",
                "password": "Strong4Password!",
                "email": "John@x.com",
                "full_name": "John Doe"
            }
        }


class User(UserBase):
    id: int
    #salary
    #dateIncrease

    class Config:
        orm_mode = True