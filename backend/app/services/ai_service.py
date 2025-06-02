import requests
from typing import Dict, List, Optional
import json
from datetime import datetime
import time
from functools import wraps

def retry_on_failure(max_retries=3, delay=1):
    """Decorator for retrying failed API calls"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    time.sleep(delay * (attempt + 1))
            return None
        return wrapper
    return decorator

class AIService:
    def __init__(self, model_name: str = "mistral"):
        """
        Initialize the AI service with Ollama.
        Args:
            model_name: The name of the model to use (default: mistral)
        """
        self.base_url = "http://localhost:11434/api"
        self.model_name = model_name

    @retry_on_failure(max_retries=3)
    def _make_api_call(self, prompt: str) -> Dict:
        """Make API call to Ollama with retry logic"""
        response = requests.post(
            f"{self.base_url}/generate",
            json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            }
        )
        
        if response.status_code != 200:
            raise Exception(f"Ollama API error: {response.status_code}")
            
        result = response.json()
        content = result.get('response', '{}')
        content = content.strip('`json\n').strip('`')
        return json.loads(content)

    def generate_task(self, 
                     challenge: str,
                     emotional_state: str,
                     energy_level: int) -> Dict:
        """
        Generate a personalized task based on user's challenge and current state.
        
        Args:
            challenge: The user's main challenge/goal
            emotional_state: Current emotional state
            energy_level: Energy level (1-10)
            
        Returns:
            Dict containing the generated task and motivational message
        """
        prompt = f"""Act as a supportive coach. The user is working on: "{challenge}".
Current emotional state: {emotional_state}
Energy level: {energy_level}/10

Generate a small, achievable task for today and a short motivational message.
Format the response as JSON with these fields:
- task: string (the specific task)
- motivation: string (a short encouraging message)
- difficulty: number (1-5)
- estimated_xp: number (10-50)

Keep the task very specific and actionable."""

        try:
            response = requests.post(
                f"{self.base_url}/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                try:
                    content = result.get('response', '{}')
                    content = content.strip('`json\n').strip('`')
                    task_data = json.loads(content)
                    return task_data
                except json.JSONDecodeError:
                    return {
                        "task": "Take a short walk and reflect on your progress",
                        "motivation": "Every small step counts towards your goal!",
                        "difficulty": 2,
                        "estimated_xp": 20
                    }
            else:
                raise Exception(f"Ollama API error: {response.status_code}")
                
        except Exception as e:
            return {
                "task": "Take a short walk and reflect on your progress",
                "motivation": "Every small step counts towards your goal!",
                "difficulty": 2,
                "estimated_xp": 20
            }

    def analyze_emotional_pattern(self, 
                                emotional_logs: List[Dict]) -> Dict:
        """
        Analyze patterns in emotional logs to provide insights.
        
        Args:
            emotional_logs: List of emotional state records
            
        Returns:
            Dict containing analysis and recommendations
        """
        log_text = "\n".join([
            f"Day {i+1}: {log.get('emotional_state', '')} - Energy: {log.get('energy_level', 0)}"
            for i, log in enumerate(emotional_logs[-7:])  # Last 7 days
        ])
        
        prompt = f"""Analyze these emotional logs and provide insights:
{log_text}

Format the response as JSON with these fields:
- pattern: string (observed pattern)
- recommendation: string (suggestion for improvement)
- positive_days: number (count of positive days)
- challenge_days: number (count of challenging days)"""

        try:
            response = requests.post(
                f"{self.base_url}/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                try:
                    content = result.get('response', '{}')
                    content = content.strip('`json\n').strip('`')
                    analysis = json.loads(content)
                    return analysis
                except json.JSONDecodeError:
                    return {
                        "pattern": "Insufficient data for pattern analysis",
                        "recommendation": "Continue logging your emotional state daily",
                        "positive_days": 0,
                        "challenge_days": 0
                    }
            else:
                raise Exception(f"Ollama API error: {response.status_code}")
                
        except Exception as e:
            return {
                "pattern": "Error analyzing patterns",
                "recommendation": "Continue logging your emotional state daily",
                "positive_days": 0,
                "challenge_days": 0
            }

    def analyze_habit_pattern(self,
                            habit_name: str,
                            completion_logs: List[Dict],
                            emotional_logs: List[Dict]) -> Dict:
        """
        Analyze habit patterns and their correlation with emotional states.
        
        Args:
            habit_name: Name of the habit being analyzed
            completion_logs: List of habit completion records
            emotional_logs: List of emotional state records
            
        Returns:
            Dict containing analysis and recommendations
        """
        # Format completion logs
        completion_text = "\n".join([
            f"Day {i+1}: {'Completed' if log.get('completed', False) else 'Missed'}"
            for i, log in enumerate(completion_logs[-14:])  # Last 14 days
        ])
        
        # Format emotional logs
        emotional_text = "\n".join([
            f"Day {i+1}: {log.get('emotional_state', '')} - Energy: {log.get('energy_level', 0)}"
            for i, log in enumerate(emotional_logs[-14:])  # Last 14 days
        ])
        
        prompt = f"""Analyze the habit "{habit_name}" and its correlation with emotional states:

Completion Logs:
{completion_text}

Emotional States:
{emotional_text}

Format the response as JSON with these fields:
- success_rate: number (percentage of successful completions)
- best_days: string (days of the week with highest success)
- emotional_correlation: string (how emotional state affects habit)
- recommendation: string (suggestion for improvement)
- streak_analysis: string (analysis of current/longest streaks)"""

        try:
            response = requests.post(
                f"{self.base_url}/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                try:
                    content = result.get('response', '{}')
                    content = content.strip('`json\n').strip('`')
                    analysis = json.loads(content)
                    return analysis
                except json.JSONDecodeError:
                    return {
                        "success_rate": 0,
                        "best_days": "Insufficient data",
                        "emotional_correlation": "Insufficient data",
                        "recommendation": "Continue tracking your habit completion",
                        "streak_analysis": "Insufficient data"
                    }
            else:
                raise Exception(f"Ollama API error: {response.status_code}")
                
        except Exception as e:
            return {
                "success_rate": 0,
                "best_days": "Error in analysis",
                "emotional_correlation": "Error in analysis",
                "recommendation": "Continue tracking your habit completion",
                "streak_analysis": "Error in analysis"
            }

    def suggest_rewards(self, user_data: Dict) -> Dict:
        """
        Suggest personalized rewards based on user's progress and preferences.
        
        Args:
            user_data: User's data including preferences and progress
            
        Returns:
            Dict containing suggested rewards
        """
        # Extract relevant user data
        level = user_data.get('level', 1)
        total_xp = user_data.get('total_xp', 0)
        preferences = user_data.get('preferences', {})
        
        prompt = f"""Suggest personalized rewards for a user with:
Level: {level}
Total XP: {total_xp}
Preferences: {json.dumps(preferences)}

Format the response as JSON with these fields:
- immediate_reward: string (reward for next achievement)
- milestone_reward: string (reward for reaching next level)
- custom_rewards: array of strings (3 personalized reward suggestions)
- xp_required: number (XP needed for next reward)"""

        try:
            response = requests.post(
                f"{self.base_url}/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                try:
                    content = result.get('response', '{}')
                    content = content.strip('`json\n').strip('`')
                    rewards = json.loads(content)
                    return rewards
                except json.JSONDecodeError:
                    return {
                        "immediate_reward": "Take a short break and enjoy a favorite snack",
                        "milestone_reward": "Plan a special activity you've been looking forward to",
                        "custom_rewards": [
                            "Watch an episode of your favorite show",
                            "Go for a walk in your favorite place",
                            "Treat yourself to something special"
                        ],
                        "xp_required": 100
                    }
            else:
                raise Exception(f"Ollama API error: {response.status_code}")
                
        except Exception as e:
            return {
                "immediate_reward": "Take a short break and enjoy a favorite snack",
                "milestone_reward": "Plan a special activity you've been looking forward to",
                "custom_rewards": [
                    "Watch an episode of your favorite show",
                    "Go for a walk in your favorite place",
                    "Treat yourself to something special"
                ],
                "xp_required": 100
            }

    def analyze_goal_progress(self,
                            goal: str,
                            current_progress: Dict,
                            historical_data: List[Dict]) -> Dict:
        """
        Analyze progress towards a goal and provide insights.
        
        Args:
            goal: The main goal being pursued
            current_progress: Current progress metrics
            historical_data: Historical progress data
            
        Returns:
            Dict containing analysis and predictions
        """
        progress_text = "\n".join([
            f"Day {i+1}: {json.dumps(log)}"
            for i, log in enumerate(historical_data[-30:])  # Last 30 days
        ])
        
        prompt = f"""Analyze progress towards this goal: "{goal}"

Current Progress:
{json.dumps(current_progress)}

Historical Data:
{progress_text}

Format the response as JSON with these fields:
- progress_percentage: number (0-100)
- estimated_completion: string (estimated completion date)
- key_milestones: array of strings (3 key milestones to reach)
- risk_factors: array of strings (potential obstacles)
- recommendations: array of strings (3 specific recommendations)
- momentum_score: number (1-10, how well progress is maintained)"""

        try:
            analysis = self._make_api_call(prompt)
            return analysis
        except Exception as e:
            return {
                "progress_percentage": 0,
                "estimated_completion": "Unable to estimate",
                "key_milestones": ["Start tracking progress", "Set clear milestones", "Review regularly"],
                "risk_factors": ["Insufficient data for analysis"],
                "recommendations": ["Continue tracking progress", "Set specific milestones", "Review weekly"],
                "momentum_score": 5
            }

    def predict_weekly_progress(self,
                              goal: str,
                              current_state: Dict,
                              historical_data: List[Dict]) -> Dict:
        """
        Predict progress for the upcoming week.
        
        Args:
            goal: The main goal being pursued
            current_state: Current state and metrics
            historical_data: Historical progress data
            
        Returns:
            Dict containing predictions and recommendations
        """
        historical_text = "\n".join([
            f"Day {i+1}: {json.dumps(log)}"
            for i, log in enumerate(historical_data[-14:])  # Last 14 days
        ])
        
        prompt = f"""Predict progress for the upcoming week for this goal: "{goal}"

Current State:
{json.dumps(current_state)}

Recent History:
{historical_text}

Format the response as JSON with these fields:
- daily_predictions: array of objects (predictions for each day)
- weekly_summary: string (overall weekly prediction)
- confidence_score: number (1-10, confidence in prediction)
- recommended_actions: array of strings (3 specific actions)
- potential_challenges: array of strings (potential obstacles)
- success_probability: number (0-100, probability of meeting goals)"""

        try:
            predictions = self._make_api_call(prompt)
            return predictions
        except Exception as e:
            return {
                "daily_predictions": [],
                "weekly_summary": "Unable to make predictions with current data",
                "confidence_score": 5,
                "recommended_actions": [
                    "Continue current routine",
                    "Track progress daily",
                    "Review goals weekly"
                ],
                "potential_challenges": ["Insufficient data for detailed prediction"],
                "success_probability": 50
            }

    def analyze_learning_pattern(self,
                               skill: str,
                               practice_logs: List[Dict],
                               emotional_logs: List[Dict]) -> Dict:
        """
        Analyze learning patterns and provide insights.
        
        Args:
            skill: The skill being learned
            practice_logs: Logs of practice sessions
            emotional_logs: Emotional state during practice
            
        Returns:
            Dict containing analysis and recommendations
        """
        practice_text = "\n".join([
            f"Session {i+1}: {json.dumps(log)}"
            for i, log in enumerate(practice_logs[-10:])  # Last 10 sessions
        ])
        
        emotional_text = "\n".join([
            f"Session {i+1}: {json.dumps(log)}"
            for i, log in enumerate(emotional_logs[-10:])  # Last 10 sessions
        ])
        
        prompt = f"""Analyze learning patterns for this skill: "{skill}"

Practice Logs:
{practice_text}

Emotional States:
{emotional_text}

Format the response as JSON with these fields:
- learning_curve: string (description of progress)
- optimal_practice_time: string (recommended practice duration)
- best_conditions: array of strings (optimal conditions for learning)
- improvement_areas: array of strings (areas needing focus)
- next_milestone: string (next learning milestone)
- estimated_mastery_time: string (estimated time to mastery)"""

        try:
            analysis = self._make_api_call(prompt)
            return analysis
        except Exception as e:
            return {
                "learning_curve": "Unable to analyze with current data",
                "optimal_practice_time": "30 minutes daily",
                "best_conditions": [
                    "Regular practice",
                    "Focused sessions",
                    "Adequate rest"
                ],
                "improvement_areas": ["Continue tracking practice sessions"],
                "next_milestone": "Set specific learning goals",
                "estimated_mastery_time": "Continue tracking progress"
            } 