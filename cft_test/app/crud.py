from sqlalchemy.orm import Session
from typing import Optional
from . import models, schemas
from .utils.hashing import get_password_hash
from datetime import date, timedelta


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100): # delete this method
    return db.query(models.User).offset(skip).limit(limit).all()


def create_salary_for_user(db: Session, db_user: models.User, salary: Optional[schemas.Salary]):
    if not salary:
        salary = schemas.Salary(salary=40000,date_increase=date.today() + timedelta(days=180))
    db_salary = models.Salary(salary=salary.salary, date_increase=salary.date_increase, user_id=db_user.id)
    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)


def get_salary_for_user(current_user:schemas.User, db: Session):
    return db.query(models.Salary).filter(current_user.id == models.Salary.user_id).first()
    # return {"salary": "here"}


def create_user(db: Session, user: schemas.UserCreate, salary: Optional[schemas.Salary]=None):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password, email=user.email, full_name = user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    create_salary_for_user(db, db_user, salary)
    return (db_user)