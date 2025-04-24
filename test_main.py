import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_schedule_task():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/tasks/", json={"duration": "5"})
    assert response.status_code == 200
    data = response.json()
    assert "task_id" in data
    assert data["status"] == "PENDING"