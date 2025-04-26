import redis
import json
import os

r = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

def set_task(task_id: str, data: dict):
    r.hset("tasks", task_id, json.dumps(data))

def get_all_tasks():
    tasks = []
    for task_id, task_data in r.hgetall("tasks").items():
        task = json.loads(task_data)
        tasks.append((task_id,task))
    return tasks

def get_task(task_id: str):
    task_data = json.loads(r.hget("tasks", task_id))
    return json.loads(task_data)

def update_task_status(task_id: str, status: str):
    task_data = json.loads(r.hget("tasks", task_id))
    task_data["status"] = status
    r.hset("tasks", task_id, json.dumps(task_data))

def update_task_result(task_id: str, result: str):
    task_data = json.loads(r.hget("tasks", task_id))
    task_data["result"] = result
    r.hset("tasks", task_id, json.dumps(task_data))