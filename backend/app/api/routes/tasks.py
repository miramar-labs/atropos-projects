from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.models.task import TaskRequest, TaskStatus
from uuid import uuid4
from app.services.task_runner import run_task
from app.crud import set_task, get_task, get_all_tasks
from typing import List

router = APIRouter(prefix="/tasks", tags=["tasks"])

# States: PENDING->RUNNING->[COMPLETED/FAILED]

@router.post("/", response_model=TaskStatus)
def create_task(task: TaskRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid4())
    set_task(task_id,{"status": "PENDING", "result": None})
    background_tasks.add_task(run_task, task_id, task.duration)
    return TaskStatus(task_id=task_id, status="PENDING")

@router.get("/{task_id}", response_model=TaskStatus)
def check_task_status(task_id: str):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskStatus(task_id=task_id, status=task['status'], result=task['result'])

@router.get('/', response_model=List[TaskStatus])
def check_all_task_statuses():
    resp=[]
    for i,(k,v) in enumerate(get_all_tasks()):
        resp.append(TaskStatus(task_id=k, status=v['status'], result=v['result']))
    return resp
