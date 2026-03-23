from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class TaskRecord:
    title: str
    question: str
    constraints: dict
    preferred_output: str
    id: UUID = field(default_factory=uuid4)
    status: str = "draft"
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class RunRecord:
    task_id: UUID
    id: UUID = field(default_factory=uuid4)
    status: str = "queued"
    started_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: datetime | None = None
    payload: dict = field(default_factory=dict)
