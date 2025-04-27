from pydantic import BaseModel

class TaskRequest(BaseModel):
    duration: int               # in seconds, to simulate long-running work
    task_id: str                # run custom task of this UUID
    uri: str | None = None      # [optional] S3 URI pointing to bucket containing task input artifacts

class TaskStatus(BaseModel):
    task_id: str                # UUID of task
    status: str                 # States: PENDING->RUNNING->[COMPLETED/FAILED]
    result: str | None = None   # [optional] string output of task (could also be an S3 URI pointing to artifacts)