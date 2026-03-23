from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import get_task_service
from app.schemas.task import TaskCreate, TaskRead
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskRead, status_code=201)
def create_task(payload: TaskCreate, service: TaskService = Depends(get_task_service)) -> TaskRead:
    return service.create_task(payload)


@router.get("", response_model=list[TaskRead])
def list_tasks(service: TaskService = Depends(get_task_service)) -> list[TaskRead]:
    return service.list_tasks()


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: UUID, service: TaskService = Depends(get_task_service)) -> TaskRead:
    task = service.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
