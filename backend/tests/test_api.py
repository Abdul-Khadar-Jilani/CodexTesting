from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthcheck() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_task_and_run_flow() -> None:
    task_response = client.post(
        "/api/tasks",
        json={
            "title": "Choose backend stack",
            "question": "Should I use FastAPI, Supabase, Groq, and Gemini for a DecisionGraph MVP?",
            "constraints": {"budget": "low"},
            "preferred_output": "memo",
        },
    )
    assert task_response.status_code == 201
    task_id = task_response.json()["id"]

    run_response = client.post("/api/runs", json={"task_id": task_id})
    assert run_response.status_code == 201
    payload = run_response.json()
    assert payload["status"] == "completed"
    assert payload["memo"]["recommendation"]
    assert len(payload["plan"]) >= 3
    assert len(payload["trace"]) >= 5
