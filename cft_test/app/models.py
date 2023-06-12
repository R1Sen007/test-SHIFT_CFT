from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, default=None)
    full_name = Column(String, default=None)
    salary = relationship("Salary", uselist=False, back_populates="user")


class Salary(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, index=True)
    salary = Column(Integer)
    date_increase = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="salary")
