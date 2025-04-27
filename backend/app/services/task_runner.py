import time,subprocess,os,sys
from app.crud import update_task_status, update_task_result

def run_task(task_id: str, duration: int, uri: str):

    filepath = "app/tasks/"+task_id+".py"

    if os.path.exists(filepath):
        # run the python script...
        update_task_status(task_id, "RUNNING")
        result = subprocess.run(
            ['python', filepath, task_id, uri],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            update_task_result(task_id, result.stdout)
            update_task_status(task_id, "COMPLETED")
        else:
            update_task_result(task_id, result.stderr)
            update_task_status(task_id, "FAILED")
    else:
        # just sleep for 'duration' secs...
        update_task_status(task_id, "RUNNING")
        try:
            time.sleep(duration)  # Simulate long task
            result = f"Task completed in {duration} seconds."
            update_task_status(task_id, "COMPLETED")
            update_task_result(task_id, result)
        except Exception as e:
            update_task_status(task_id, "FAILED")
            update_task_status(task_id, str(e))


