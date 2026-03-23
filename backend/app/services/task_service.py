from uuid import UUID

from app.db.models import TaskRecord
from app.repositories.in_memory import InMemoryRepository
from app.schemas.task import TaskCreate, TaskRead


class TaskService:
    def __init__(self, repository: InMemoryRepository) -> None:
        self.repository = repository

    def create_task(self, payload: TaskCreate) -> TaskRead:
        record = TaskRecord(
            title=payload.title,
            question=payload.question,
            constraints=payload.constraints,
            preferred_output=payload.preferred_output,
            status="queued",
        )
        self.repository.create_task(record)
        return TaskRead.model_validate(record.__dict__)

    def list_tasks(self) -> list[TaskRead]:
        return [TaskRead.model_validate(task.__dict__) for task in self.repository.list_tasks()]

    def get_task(self, task_id: UUID):
        task = self.repository.get_task(task_id)
        if not task:
            return None
        return TaskRead.model_validate(task.__dict__)
