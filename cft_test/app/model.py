from typing import Union
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    username: str 
    password: str
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


class UserLogin(BaseModel):
    username: str 
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "ProUser007",
                "password": "Strong4Password!",
            }
        }