from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import BaseModel

class Reward(BaseModel):
    __tablename__ = "rewards"

    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, index=True)
    description = Column(String)
    points_required = Column(Integer)
    category = Column(String)
    redeemed = Column(Boolean, default=False)
    redeemed_at = Column(Date, nullable=True)

    user = relationship("User", back_populates="rewards") 