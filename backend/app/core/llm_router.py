from dataclasses import dataclass
from typing import Literal

from app.core.config import get_settings

TaskType = Literal["parse", "planner", "research", "critic", "synthesis"]


@dataclass(frozen=True)
class ModelSelection:
    provider: str
    model: str
    reason: str


class LLMRouter:
    def __init__(self) -> None:
        self.settings = get_settings()

    def select_model(self, task_type: TaskType) -> ModelSelection:
        if task_type == "parse":
            return ModelSelection(
                provider="groq",
                model=self.settings.planner_model,
                reason="Fast structured parsing and task classification.",
            )
        if task_type == "planner":
            return ModelSelection(
                provider="groq",
                model=self.settings.planner_model,
                reason="Low-latency planning for workflow generation.",
            )
        if task_type == "research":
            return ModelSelection(
                provider="groq",
                model=self.settings.research_model,
                reason="Efficient subtask summarization and evidence extraction.",
            )
        if task_type == "critic":
            return ModelSelection(
                provider="groq",
                model=self.settings.critic_model,
                reason="Higher-capacity critique for gap detection.",
            )
        return ModelSelection(
            provider="gemini",
            model=self.settings.synthesis_model,
            reason="Long-context final synthesis and recommendation writing.",
        )
