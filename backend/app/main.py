from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import tasks, habits, rewards, analytics, auth
from app.core.config import settings

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
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(habits.router, prefix="/api/habits", tags=["Habits"])
app.include_router(rewards.router, prefix="/api/rewards", tags=["Rewards"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])

@app.get("/")
async def root():
    return {"message": "Welcome to InnerLevel API"} 