from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict
from pydantic import BaseModel
from ..services.ai_service import AIService
from ..auth import get_current_user

router = APIRouter(prefix="/ai", tags=["ai"])

# Initialize AI service
ai_service = AIService()

class TaskGenerationRequest(BaseModel):
    challenge: str
    emotional_state: str
    energy_level: int

class EmotionalLog(BaseModel):
    emotional_state: str
    energy_level: int
    date: str
    notes: str = ""

class HabitAnalysisRequest(BaseModel):
    habit_name: str
    completion_logs: List[Dict]
    emotional_logs: List[EmotionalLog]

class GoalAnalysisRequest(BaseModel):
    goal: str
    current_progress: Dict
    historical_data: List[Dict]

class ProgressPredictionRequest(BaseModel):
    goal: str
    current_state: Dict
    historical_data: List[Dict]

class LearningAnalysisRequest(BaseModel):
    skill: str
    practice_logs: List[Dict]
    emotional_logs: List[Dict]

@router.post("/generate-task")
async def generate_task(
    request: TaskGenerationRequest,
    current_user: Dict = Depends(get_current_user)
):
    """
    Generate a personalized task based on user's challenge and current state.
    """
    try:
        task = ai_service.generate_task(
            challenge=request.challenge,
            emotional_state=request.emotional_state,
            energy_level=request.energy_level
        )
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-emotions")
async def analyze_emotions(
    emotional_logs: List[EmotionalLog],
    current_user: Dict = Depends(get_current_user)
):
    """
    Analyze emotional patterns and provide insights.
    """
    try:
        analysis = ai_service.analyze_emotional_pattern(emotional_logs)
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-habit")
async def analyze_habit(
    request: HabitAnalysisRequest,
    current_user: Dict = Depends(get_current_user)
):
    """
    Analyze habit patterns and their correlation with emotional states.
    """
    try:
        analysis = ai_service.analyze_habit_pattern(
            habit_name=request.habit_name,
            completion_logs=request.completion_logs,
            emotional_logs=request.emotional_logs
        )
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/suggest-rewards")
async def suggest_rewards(
    current_user: Dict = Depends(get_current_user)
):
    """
    Suggest personalized rewards based on user's progress and preferences.
    """
    try:
        rewards = ai_service.suggest_rewards(current_user)
        return rewards
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-goal")
async def analyze_goal(
    request: GoalAnalysisRequest,
    current_user: Dict = Depends(get_current_user)
):
    """
    Analyze progress towards a goal and provide insights.
    """
    try:
        analysis = ai_service.analyze_goal_progress(
            goal=request.goal,
            current_progress=request.current_progress,
            historical_data=request.historical_data
        )
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict-progress")
async def predict_progress(
    request: ProgressPredictionRequest,
    current_user: Dict = Depends(get_current_user)
):
    """
    Predict progress for the upcoming week.
    """
    try:
        predictions = ai_service.predict_weekly_progress(
            goal=request.goal,
            current_state=request.current_state,
            historical_data=request.historical_data
        )
        return predictions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-learning")
async def analyze_learning(
    request: LearningAnalysisRequest,
    current_user: Dict = Depends(get_current_user)
):
    """
    Analyze learning patterns and provide insights.
    """
    try:
        analysis = ai_service.analyze_learning_pattern(
            skill=request.skill,
            practice_logs=request.practice_logs,
            emotional_logs=request.emotional_logs
        )
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 