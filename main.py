from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from uuid import uuid4
import time
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Simple In-memory store for task statuses and results (dict)
tasks = {}

class TaskRequest(BaseModel):
    duration: int               # in seconds, to simulate long-running work

class TaskStatus(BaseModel):
    task_id: str
    status: str
    result: str | None = None

def long_running_task(task_id: str, duration: int):
    tasks[task_id]['status'] = 'IN_PROGRESS'
    try:
        time.sleep(duration)  # Simulate long task
        result = f"Task completed in {duration} seconds."
        tasks[task_id]['status'] = 'COMPLETED'
        tasks[task_id]['result'] = result
    except Exception as e:
        tasks[task_id]['status'] = 'FAILED'
        tasks[task_id]['result'] = str(e)

# ROUTES (define these early!) 
@app.post("/api/v1/tasks/", response_model=TaskStatus)
def create_task(task: TaskRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid4())
    tasks[task_id] = {"status": "PENDING", "result": None}
    background_tasks.add_task(long_running_task, task_id, task.duration)
    return TaskStatus(task_id=task_id, status="PENDING")

@app.get("/api/v1/tasks/{task_id}", response_model=TaskStatus)
def check_task_status(task_id: str):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskStatus(task_id=task_id, status=task['status'], result=task['result'])

@app.get('/api/v1/tasks/', response_model=List[TaskStatus])
def check_all_task_statuses():
    resp=[]
    for i,(k,v) in enumerate(tasks.items()):
        resp.append(TaskStatus(task_id=k, status=v['status'], result=v['result']))
    return resp

# Serve frontend UI
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":    
    uvicorn.run(app, host='0.0.0.0', port=8000)