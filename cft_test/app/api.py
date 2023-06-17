from typing import Union, Annotated, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import get_db, engine
from .auth.auth_handler import authenticate_user, create_access_token, get_current_user

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", tags=["root"])
def read_root():
    return {"Hello": "World"}


@app.get("/users/", tags=["user"], response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/users/signup", tags=["user"], response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db), salary: Optional[schemas.Salary]= None):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user: 
        raise HTTPException(status_code=400, detail="Username reserved")
    return crud.create_user(db=db, user=user)


@app.post("/users/login", tags=["user"], response_model=schemas.Token)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/salary", tags=["user"], response_model=schemas.Salary)
def get_salary(current_user: Annotated[schemas.User, Depends(get_current_user)], db: Session = Depends(get_db)): # как передать сюда дб?
    salary = crud.get_salary_for_user(current_user, db)
    return salary