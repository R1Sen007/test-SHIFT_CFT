from typing import Union
from datetime import date
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
            "examples":{
                "normal": {
                    "summary": "Full example",
                    "description": "-----",
                    "value": {
                        "username": "ProUser007",
                        "password": "Strong4Password!",
                        "email": "John@x.com",
                        "full_name": "John Doe"
                    }
                },
                "converted": {
                    "summary": "Minimal example",
                    "description": "required params",
                    "value": {
                        "username": "ProUser007",
                        "password": "Strong4Password!",
                    }
                }
            }
        }


class User(UserBase):
    id: int
    #salary
    #dateIncrease

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class Salary(BaseModel):
    salary: int
    date_increase: date

    class Config:
        orm_mode = True