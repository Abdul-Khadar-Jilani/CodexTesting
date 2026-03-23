from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import get_run_service
from app.schemas.run import RunCreate, RunRead
from app.services.run_service import RunService

router = APIRouter(prefix="/runs", tags=["runs"])


@router.post("", response_model=RunRead, status_code=201)
def create_run(payload: RunCreate, service: RunService = Depends(get_run_service)) -> RunRead:
    run = service.create_run(payload.task_id)
    if run is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return run


@router.get("/{run_id}", response_model=RunRead)
def get_run(run_id: UUID, service: RunService = Depends(get_run_service)) -> RunRead:
    run = service.get_run(run_id)
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")
    return run
