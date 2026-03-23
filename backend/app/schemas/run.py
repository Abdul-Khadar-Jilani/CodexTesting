from datetime import datetime
from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from app.schemas.agent import AgentTrace, CritiqueResult, EvidenceItem, FinalMemo, PlanItem


class RunCreate(BaseModel):
    task_id: UUID


class RunRead(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    task_id: UUID
    status: Literal["queued", "running", "completed", "failed"] = "queued"
    started_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: datetime | None = None
    plan: list[PlanItem] = Field(default_factory=list)
    evidence: list[EvidenceItem] = Field(default_factory=list)
    critique: CritiqueResult | None = None
    memo: FinalMemo | None = None
    trace: list[AgentTrace] = Field(default_factory=list)
