from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    priority: str
    status: str
    points: int
    category: str
    emotional_state_before: Optional[str] = None
    emotional_state_after: Optional[str] = None
    energy_level: Optional[int] = None
    comment: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    points: Optional[int] = None
    category: Optional[str] = None
    emotional_state_before: Optional[str] = None
    emotional_state_after: Optional[str] = None
    energy_level: Optional[int] = None
    comment: Optional[str] = None

class TaskResponse(TaskBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 