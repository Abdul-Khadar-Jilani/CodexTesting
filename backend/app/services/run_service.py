from datetime import datetime
from uuid import UUID

from app.db.models import RunRecord
from app.graph.builder import execute_workflow
from app.graph.state import GraphState
from app.repositories.in_memory import InMemoryRepository
from app.schemas.run import RunRead


class RunService:
    def __init__(self, repository: InMemoryRepository) -> None:
        self.repository = repository

    def create_run(self, task_id: UUID) -> RunRead | None:
        task = self.repository.get_task(task_id)
        if not task:
            return None

        self.repository.update_task_status(task_id, "running")
        run_record = RunRecord(task_id=task_id, status="running")
        self.repository.create_run(run_record)

        initial_state: GraphState = {
            "task_id": task.id,
            "task_title": task.title,
            "question": task.question,
            "constraints": task.constraints,
            "preferred_output": task.preferred_output,
            "trace": [],
        }
        state = execute_workflow(initial_state)
        payload = {
            "plan": [item.model_dump() for item in state.get("plan", [])],
            "evidence": [item.model_dump() for item in state.get("evidence", [])],
            "critique": state["critique"].model_dump() if state.get("critique") else None,
            "memo": state["memo"].model_dump() if state.get("memo") else None,
            "trace": [item.model_dump() for item in state.get("trace", [])],
        }
        self.repository.update_run(run_record.id, status="completed", payload=payload)
        self.repository.update_task_status(task_id, "completed")

        completed = self.repository.get_run(run_record.id)
        return RunRead(
            id=completed.id,
            task_id=completed.task_id,
            status=completed.status,
            started_at=completed.started_at,
            completed_at=completed.completed_at or datetime.utcnow(),
            **completed.payload,
        )

    def get_run(self, run_id: UUID) -> RunRead | None:
        run = self.repository.get_run(run_id)
        if not run:
            return None
        return RunRead(
            id=run.id,
            task_id=run.task_id,
            status=run.status,
            started_at=run.started_at,
            completed_at=run.completed_at,
            **run.payload,
        )
