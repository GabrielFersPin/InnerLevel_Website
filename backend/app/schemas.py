from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    name: str
    points: int
    category: str
    status: str
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True

class HabitBase(BaseModel):
    name: str
    category: str
    points: int

class HabitCreate(HabitBase):
    pass

class Habit(HabitBase):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True

class RewardBase(BaseModel):
    name: str
    description: str
    points_required: int
    category: str

class RewardCreate(RewardBase):
    pass

class Reward(RewardBase):
    id: int
    redeemed: bool
    redeemed_at: Optional[datetime]
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True

class EmotionalLogBase(BaseModel):
    date: datetime
    morning_emotion: str
    morning_energy: int
    morning_notes: Optional[str]
    evening_emotion: str
    evening_energy: int
    evening_notes: Optional[str]
    gratitude: str

class EmotionalLogCreate(EmotionalLogBase):
    pass

class EmotionalLog(EmotionalLogBase):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None 