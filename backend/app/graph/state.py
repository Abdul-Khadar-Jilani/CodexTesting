from typing import Any, TypedDict
from uuid import UUID

from app.schemas.agent import AgentTrace, CritiqueResult, EvidenceItem, FinalMemo, PlanItem


class GraphState(TypedDict, total=False):
    task_id: UUID
    task_title: str
    question: str
    constraints: dict[str, Any]
    preferred_output: str
    plan: list[PlanItem]
    evidence: list[EvidenceItem]
    critique: CritiqueResult
    memo: FinalMemo
    trace: list[AgentTrace]
