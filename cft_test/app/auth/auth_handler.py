from app.schemas import UserLogin, TokenData
from app.crud import get_user_by_username
from app.utils.hashing import verify_password
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Annotated

SECRET_KEY = "aed020f9e60d26443086bc347d3d5c4b92e9999b392d3f7eaebe81193e9a7856" # MUST BE IN ENV VAR
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 30 # TIME OF LIFE TOKEN IN MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict):
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    expire = datetime.utcnow() + expires_delta
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)): #  как передать сюда базу?
    credentials_exeption = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exeption
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exeption
    user = get_user_by_username(db, username=username) 
    if user is None:
        raise credentials_exeption
    return user