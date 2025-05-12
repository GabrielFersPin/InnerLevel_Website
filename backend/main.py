from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    name: str
    points: int
    mood_before: str
    mood_after: str

@app.post("/task")
async def create_task(task: Task):
    # Here you would typically save the task to your database
    # For now, we'll just return a success message
    return {"status": "success", "message": f"Task '{task.name}' created successfully"} 