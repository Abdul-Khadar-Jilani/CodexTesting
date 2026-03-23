from datetime import datetime
from typing import Any, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    question: str = Field(min_length=10, max_length=4000)
    constraints: dict[str, Any] = Field(default_factory=dict)
    preferred_output: Literal["memo", "brief", "comparison"] = "memo"


class TaskRead(TaskCreate):
    id: UUID = Field(default_factory=uuid4)
    status: Literal["draft", "queued", "running", "completed", "failed"] = "draft"
    created_at: datetime = Field(default_factory=datetime.utcnow)
