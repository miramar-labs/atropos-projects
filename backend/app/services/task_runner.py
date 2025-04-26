import time
from app.crud import update_task_status, update_task_result

def run_task(task_id: str, duration: int):
    update_task_status(task_id, "RUNNING")
    try:
        time.sleep(duration)  # Simulate long task
        result = f"Task completed in {duration} seconds."
        update_task_status(task_id, "COMPLETED")
        update_task_result(task_id, result)
    except Exception as e:
        update_task_status(task_id, "FAILED")
        update_task_status(task_id, str(e))
