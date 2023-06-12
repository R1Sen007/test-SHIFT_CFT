from typing import Union
from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["root"])
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.post("/user/signup", tags=["user"])
# async def create_user(user: User = Body(...)):
#     return {"message": "user signed up!"}

@app.get("/users/", tags=["user"], response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/users/signup", tags=["user"], response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print(user)
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user: 
        raise HTTPException(status_code=400, detail="Username reserved")
    return crud.create_user(db=db, user=user)
