# 🌱 RaízXP – Personal Growth & Motivation Tracker

**RaízXP** is a personal gamification system designed to help you stay focused, motivated, and emotionally regulated while working toward your goals — whether you're job hunting, building habits, or trying to stay grounded in difficult times.

This project was born from my own need to manage energy, emotions, and progress in a way that typical productivity apps couldn't offer me. So I built it — first with Streamlit, now evolving into a full web app.

---

## 🎯 What does this app do?

- Register daily personal or professional tasks
- Assign XP points and track your level
- Record emotional state before/after each activity
- Visualize your weekly growth and energy patterns
- Get simple recommendations to regulate your mood and focus

---

## ⚙️ Tech Stack

| Layer     | Tools Used                  |
|-----------|-----------------------------|
| Frontend  | React + Vite + Tailwind CSS |
| Backend   | FastAPI                     |
| Storage   | CSV (local) or Supabase (planned) |
| Deployment | Vercel (frontend) + Render (backend) |

---

## 🧠 Data Science Focus

While this is a full-stack project, the core logic revolves around:

- Self-tracking and behavioral data collection
- Emotional state analysis
- Habit-impact correlation analysis
- Simple recommender logic for personal well-being
- Potential future integration of ML models (emotional prediction or personalized action suggestions)

---

## 🚀 How to run locally

### Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

```

# InnerLevel - Personal Development Web Application

A modern web application for tracking personal development, habits, and emotional well-being.

## Features

- User authentication (login/register)
- Task management with points system
- Habit tracking
- Reward system
- Emotional logging
- Modern, responsive UI with Tailwind CSS

## Tech Stack

### Backend
- FastAPI (Python)
- PostgreSQL
- SQLAlchemy
- JWT Authentication

### Frontend
- React
- TypeScript
- Tailwind CSS
- React Router
- Axios

## Prerequisites

- Python 3.8+
- Node.js 14+
- PostgreSQL

## Setup

### Backend Setup

1. Create a virtual environment and activate it:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the backend directory with the following content:
```
DATABASE_URL=postgresql://postgres:postgres@localhost/innerlevel
SECRET_KEY=your-super-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. Create the PostgreSQL database:
```bash
createdb innerlevel
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

## Running the Application

1. Start the backend server:
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn app.main:app --reload
```

2. Start the frontend development server:
```bash
cd frontend
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## API Endpoints

- POST /token - Get access token
- POST /users/ - Create new user
- GET /tasks/ - Get user's tasks
- POST /tasks/ - Create new task
- GET /habits/ - Get user's habits
- POST /habits/ - Create new habit
- GET /rewards/ - Get user's rewards
- POST /rewards/ - Create new reward
- GET /emotional-logs/ - Get user's emotional logs
- POST /emotional-logs/ - Create new emotional log

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
