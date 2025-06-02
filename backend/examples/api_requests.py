import requests
import json
from datetime import datetime, timedelta

# Base URL for the API
BASE_URL = "http://localhost:8000"

# Example authentication
def get_auth_token():
    response = requests.post(
        f"{BASE_URL}/token",
        data={
            "username": "user@example.com",
            "password": "password123"
        }
    )
    return response.json()["access_token"]

# Example: Generate a task
def generate_task_example():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    data = {
        "challenge": "Learn Python programming",
        "emotional_state": "motivated but tired",
        "energy_level": 7
    }
    
    response = requests.post(
        f"{BASE_URL}/ai/generate-task",
        headers=headers,
        json=data
    )
    return response.json()

# Example: Analyze emotional patterns
def analyze_emotions_example():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    # Generate last 7 days of emotional logs
    emotional_logs = [
        {
            "emotional_state": "energetic",
            "energy_level": 8,
            "date": (datetime.now() - timedelta(days=i)).isoformat(),
            "notes": "Feeling productive"
        }
        for i in range(7)
    ]
    
    response = requests.post(
        f"{BASE_URL}/ai/analyze-emotions",
        headers=headers,
        json=emotional_logs
    )
    return response.json()

# Example: Analyze habit patterns
def analyze_habit_example():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    data = {
        "habit_name": "Daily coding practice",
        "completion_logs": [
            {
                "date": (datetime.now() - timedelta(days=i)).isoformat(),
                "completed": i % 2 == 0,  # Alternate between completed and missed
                "duration": 30
            }
            for i in range(14)
        ],
        "emotional_logs": [
            {
                "emotional_state": "focused" if i % 2 == 0 else "distracted",
                "energy_level": 7 if i % 2 == 0 else 5,
                "date": (datetime.now() - timedelta(days=i)).isoformat(),
                "notes": "Regular practice session"
            }
            for i in range(14)
        ]
    }
    
    response = requests.post(
        f"{BASE_URL}/ai/analyze-habit",
        headers=headers,
        json=data
    )
    return response.json()

# Example: Analyze goal progress
def analyze_goal_example():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    data = {
        "goal": "Complete Python web development course",
        "current_progress": {
            "completed_modules": 5,
            "total_modules": 10,
            "current_streak": 7,
            "last_activity": datetime.now().isoformat()
        },
        "historical_data": [
            {
                "date": (datetime.now() - timedelta(days=i)).isoformat(),
                "modules_completed": i // 2,
                "practice_time": 45,
                "quiz_score": 85
            }
            for i in range(30)
        ]
    }
    
    response = requests.post(
        f"{BASE_URL}/ai/analyze-goal",
        headers=headers,
        json=data
    )
    return response.json()

# Example: Predict weekly progress
def predict_progress_example():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    data = {
        "goal": "Complete Python web development course",
        "current_state": {
            "completed_modules": 5,
            "current_streak": 7,
            "average_daily_time": 45,
            "last_activity": datetime.now().isoformat()
        },
        "historical_data": [
            {
                "date": (datetime.now() - timedelta(days=i)).isoformat(),
                "modules_completed": i // 2,
                "practice_time": 45,
                "quiz_score": 85
            }
            for i in range(14)
        ]
    }
    
    response = requests.post(
        f"{BASE_URL}/ai/predict-progress",
        headers=headers,
        json=data
    )
    return response.json()

# Example: Analyze learning patterns
def analyze_learning_example():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    data = {
        "skill": "Python programming",
        "practice_logs": [
            {
                "date": (datetime.now() - timedelta(days=i)).isoformat(),
                "duration": 45,
                "topics_covered": ["functions", "classes", "decorators"],
                "difficulty_level": 3,
                "completion_rate": 0.8
            }
            for i in range(10)
        ],
        "emotional_logs": [
            {
                "emotional_state": "focused" if i % 2 == 0 else "tired",
                "energy_level": 7 if i % 2 == 0 else 5,
                "date": (datetime.now() - timedelta(days=i)).isoformat(),
                "notes": "Regular practice session"
            }
            for i in range(10)
        ]
    }
    
    response = requests.post(
        f"{BASE_URL}/ai/analyze-learning",
        headers=headers,
        json=data
    )
    return response.json()

if __name__ == "__main__":
    # Test all endpoints
    print("\nGenerating task...")
    print(json.dumps(generate_task_example(), indent=2))
    
    print("\nAnalyzing emotions...")
    print(json.dumps(analyze_emotions_example(), indent=2))
    
    print("\nAnalyzing habit...")
    print(json.dumps(analyze_habit_example(), indent=2))
    
    print("\nAnalyzing goal...")
    print(json.dumps(analyze_goal_example(), indent=2))
    
    print("\nPredicting progress...")
    print(json.dumps(predict_progress_example(), indent=2))
    
    print("\nAnalyzing learning patterns...")
    print(json.dumps(analyze_learning_example(), indent=2)) 