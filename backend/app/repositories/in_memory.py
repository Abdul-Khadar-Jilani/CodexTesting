from collections.abc import Iterable
from datetime import datetime
from uuid import UUID

from app.db.models import RunRecord, TaskRecord


class InMemoryRepository:
    def __init__(self) -> None:
        self.tasks: dict[UUID, TaskRecord] = {}
        self.runs: dict[UUID, RunRecord] = {}

    def create_task(self, record: TaskRecord) -> TaskRecord:
        self.tasks[record.id] = record
        return record

    def list_tasks(self) -> Iterable[TaskRecord]:
        return self.tasks.values()

    def get_task(self, task_id: UUID) -> TaskRecord | None:
        return self.tasks.get(task_id)

    def update_task_status(self, task_id: UUID, status: str) -> None:
        if task_id in self.tasks:
            self.tasks[task_id].status = status

    def create_run(self, record: RunRecord) -> RunRecord:
        self.runs[record.id] = record
        return record

    def get_run(self, run_id: UUID) -> RunRecord | None:
        return self.runs.get(run_id)

    def list_runs(self) -> Iterable[RunRecord]:
        return self.runs.values()

    def update_run(self, run_id: UUID, *, status: str, payload: dict) -> None:
        if run_id in self.runs:
            self.runs[run_id].status = status
            self.runs[run_id].payload = payload
            self.runs[run_id].completed_at = datetime.utcnow()
