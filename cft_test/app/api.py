from typing import Union
from fastapi import FastAPI, Body
from .model import User, UserLogin

app = FastAPI()


@app.get("/", tags=["root"])
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/user/signup", tags=["user"])
async def create_user(user: User = Body(...)):
    return {"message": "user signed up!"}