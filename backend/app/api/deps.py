from functools import lru_cache

from app.repositories.in_memory import InMemoryRepository
from app.services.run_service import RunService
from app.services.task_service import TaskService


@lru_cache
def get_repository() -> InMemoryRepository:
    return InMemoryRepository()


def get_task_service() -> TaskService:
    return TaskService(get_repository())


def get_run_service() -> RunService:
    return RunService(get_repository())
