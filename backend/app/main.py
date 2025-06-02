from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List
from . import models, schemas, auth
from .database import engine, get_db
from .api import ai  # Import the AI router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="InnerLevel API",
    description="Backend API for InnerLevel - Gamification Tracker",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ai.router)  # Add the AI router

# Authentication endpoints
@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Task endpoints
@app.post("/tasks/", response_model=schemas.Task)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    db_task = models.Task(**task.dict(), owner_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    tasks = db.query(models.Task).filter(models.Task.owner_id == current_user.id).offset(skip).limit(limit).all()
    return tasks

# Habit endpoints
@app.post("/habits/", response_model=schemas.Habit)
def create_habit(
    habit: schemas.HabitCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    db_habit = models.Habit(**habit.dict(), owner_id=current_user.id)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

@app.get("/habits/", response_model=List[schemas.Habit])
def read_habits(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    habits = db.query(models.Habit).filter(models.Habit.owner_id == current_user.id).offset(skip).limit(limit).all()
    return habits

# Reward endpoints
@app.post("/rewards/", response_model=schemas.Reward)
def create_reward(
    reward: schemas.RewardCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    db_reward = models.Reward(**reward.dict(), owner_id=current_user.id)
    db.add(db_reward)
    db.commit()
    db.refresh(db_reward)
    return db_reward

@app.get("/rewards/", response_model=List[schemas.Reward])
def read_rewards(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    rewards = db.query(models.Reward).filter(models.Reward.owner_id == current_user.id).offset(skip).limit(limit).all()
    return rewards

# Emotional log endpoints
@app.post("/emotional-logs/", response_model=schemas.EmotionalLog)
def create_emotional_log(
    emotional_log: schemas.EmotionalLogCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    db_emotional_log = models.EmotionalLog(**emotional_log.dict(), owner_id=current_user.id)
    db.add(db_emotional_log)
    db.commit()
    db.refresh(db_emotional_log)
    return db_emotional_log

@app.get("/emotional-logs/", response_model=List[schemas.EmotionalLog])
def read_emotional_logs(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    emotional_logs = db.query(models.EmotionalLog).filter(
        models.EmotionalLog.owner_id == current_user.id
    ).offset(skip).limit(limit).all()
    return emotional_logs

@app.get("/")
async def root():
    return {"message": "Welcome to InnerLevel API"} 