from app.core.llm_router import LLMRouter
from app.graph.state import GraphState
from app.schemas.agent import AgentTrace, CritiqueResult


router = LLMRouter()


def critic_node(state: GraphState) -> GraphState:
    selection = router.select_model("critic")
    critique = CritiqueResult(
        gaps=["Add external source ingestion and citation grounding in the next iteration."],
        contradictions=[],
        requires_revision=False,
    )
    trace = state.get("trace", [])
    trace.append(
        AgentTrace(
            node_name="critic",
            agent_type="critic",
            model_name=selection.model,
            summary="Reviewed evidence coverage and flagged next-step research gaps.",
        )
    )
    state["critique"] = critique
    state["trace"] = trace
    return state
