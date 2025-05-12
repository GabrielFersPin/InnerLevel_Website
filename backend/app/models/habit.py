from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Habit(BaseModel):
    __tablename__ = "habits"

    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, index=True)
    category = Column(String)  # Professional, Personal, Self-Care
    points = Column(Integer)
    description = Column(String, nullable=True)

    user = relationship("User", back_populates="habits") 