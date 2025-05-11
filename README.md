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
