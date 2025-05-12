from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Task(BaseModel):
    __tablename__ = "tasks"

    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    due_date = Column(Date)
    priority = Column(String)  # High, Medium, Low
    status = Column(String)  # Pending, In Progress, Completed
    points = Column(Integer)
    category = Column(String)  # Professional, Personal, Self-Care
    emotional_state_before = Column(String, nullable=True)
    emotional_state_after = Column(String, nullable=True)
    energy_level = Column(Integer, nullable=True)
    comment = Column(String, nullable=True)

    user = relationship("User", back_populates="tasks") 