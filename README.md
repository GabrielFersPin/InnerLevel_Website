# 🌱 RaízXP – Personal Growth & Motivation Tracker

**RaízXP** (formerly known as "Desafío Inteligente") is an AI-powered personal development platform designed to help you stay focused, motivated, and emotionally regulated while working toward your goals. Whether you're job hunting, building habits, or trying to stay grounded in difficult times, RaízXP adapts to your emotional state and energy levels to provide personalized guidance.

## 🎯 Core Features

### Challenge-Based Growth
- Select a personal challenge (e.g., landing your first data science job)
- Get AI-generated tasks tailored to your current state
- Track progress through levels and achievements

### Emotional Intelligence
- Daily emotional and energy state tracking
- AI-powered task adaptation based on your mood
- Personalized motivational messages

### Gamification System
- XP points for completed tasks
- Level progression
- Customizable rewards system
- Achievement tracking

### Smart Analytics
- Visualize your emotional patterns
- Track energy levels over time
- Monitor progress toward your goals
- Get personalized insights

## ⚙️ Tech Stack

| Layer     | Tools Used                  |
|-----------|-----------------------------|
| Frontend  | React + Vite + Tailwind CSS |
| Backend   | FastAPI                     |
| Database  | PostgreSQL                  |
| AI        | OpenAI API (planned)        |
| Auth      | JWT Authentication          |
| Deployment| Vercel (frontend) + Render (backend) |

## 🧠 AI Integration

The platform uses AI to:
- Generate personalized daily tasks
- Adapt difficulty based on emotional state
- Provide motivational messages
- Analyze patterns in user behavior
- Suggest optimal reward strategies

## 🚀 Getting Started

### Backend Setup

1. Create and activate virtual environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create .env file with:
DATABASE_URL=postgresql://postgres:postgres@localhost/raizxp
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-key  # For AI features
```

4. Initialize database:
```bash
createdb raizxp
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Start development server:
```bash
npm run dev
```

## 📚 API Documentation

Key endpoints:
- `/api/auth/*` - Authentication endpoints
- `/api/challenges/*` - Challenge management
- `/api/tasks/*` - AI-generated task management
- `/api/emotions/*` - Emotional state tracking
- `/api/rewards/*` - Reward system
- `/api/analytics/*` - Progress and pattern analysis

Full API documentation available at `/docs` when running the backend server.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

MIT License - See LICENSE file for details
