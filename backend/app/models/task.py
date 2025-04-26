from pydantic import BaseModel

class TaskRequest(BaseModel):
    duration: int               # in seconds, to simulate long-running work

class TaskStatus(BaseModel):
    task_id: str
    status: str
    result: str | None = None