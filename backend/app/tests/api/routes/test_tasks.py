import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch
from app.main import app
from app.crud import r  # Redis client

@pytest.fixture(autouse=True)
def clear_redis():
    """Clear Redis before each test"""
    r.flushall()

@pytest.mark.asyncio
async def test_create_task_simple():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/tasks/", json={
            "duration": "5",
            "task_id":"",
            "uri":""
            })
    assert response.status_code == 200
    data = response.json()
    assert "task_id" in data
    assert data["status"] == "PENDING"

# TODO test_check_task_status():

@pytest.mark.asyncio
async def test_check_all_task_statuses():
    # create a dummy task and check it shows up in status list
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        await ac.post("/api/v1/tasks/", json={
            "duration": "5",
            "task_id":"",
            "uri":""
            })
        response = await ac.get("/api/v1/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert all("task_id" in task and "result" in task and "status" in task for task in data)

@pytest.mark.asyncio
async def test_background_task_completion():
    with patch("app.services.task_runner.time.sleep", return_value=None):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            response = await ac.post("/api/v1/tasks/", json={
            "duration": "5",
            "task_id":"",
            "uri":""
            })
            task_id = response.json()["task_id"]

        # Import and manually call the background task logic
        from app.services.task_runner import run_task
        run_task(task_id, 5, "")  # No sleep, immediately completes

        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            response = await ac.get("/api/v1/tasks/")
            tasks = response.json()

        completed = any(task["task_id"] == task_id and task["status"] == "COMPLETED" for task in tasks)
        assert completed
