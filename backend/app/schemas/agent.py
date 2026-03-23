from typing import Literal

from pydantic import BaseModel, Field


class PlanItem(BaseModel):
    title: str
    description: str
    priority: int = Field(ge=1, le=5, default=3)


class EvidenceItem(BaseModel):
    subtask_title: str
    claim: str
    supporting_text: str
    source_label: str
    confidence: float = Field(ge=0.0, le=1.0)


class CritiqueResult(BaseModel):
    gaps: list[str] = Field(default_factory=list)
    contradictions: list[str] = Field(default_factory=list)
    requires_revision: bool = False


class MemoSection(BaseModel):
    heading: str
    content: str


class FinalMemo(BaseModel):
    executive_summary: str
    recommendation: str
    confidence_score: float = Field(ge=0.0, le=1.0)
    sections: list[MemoSection] = Field(default_factory=list)


class AgentTrace(BaseModel):
    node_name: str
    agent_type: Literal["planner", "research", "critic", "synthesis", "system"]
    model_name: str
    summary: str
