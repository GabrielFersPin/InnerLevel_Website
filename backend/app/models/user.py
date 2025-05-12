from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .base import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    total_points = Column(Integer, default=0)
    available_points = Column(Integer, default=0)

    tasks = relationship("Task", back_populates="user")
    habits = relationship("Habit", back_populates="user")
    rewards = relationship("Reward", back_populates="user") 