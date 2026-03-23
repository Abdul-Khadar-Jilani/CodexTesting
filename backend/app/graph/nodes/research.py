from app.core.llm_router import LLMRouter
from app.graph.state import GraphState
from app.schemas.agent import AgentTrace, EvidenceItem


router = LLMRouter()


def research_node(state: GraphState) -> GraphState:
    selection = router.select_model("research")
    title = state.get("task_title", "the task")
    evidence = [
        EvidenceItem(
            subtask_title="Technical options",
            claim=f"{title} benefits from a modular FastAPI + Supabase backend architecture.",
            supporting_text="Separating API, orchestration, and persistence keeps the system easy to evolve.",
            source_label="internal-seed",
            confidence=0.82,
        ),
        EvidenceItem(
            subtask_title="Model routing",
            claim="Using Groq for planning/research and Gemini for synthesis balances cost and quality.",
            supporting_text="Different workflow nodes have different latency and reasoning requirements.",
            source_label="internal-seed",
            confidence=0.8,
        ),
    ]
    trace = state.get("trace", [])
    trace.append(
        AgentTrace(
            node_name="research",
            agent_type="research",
            model_name=selection.model,
            summary="Collected initial evidence for architecture and model-routing decisions.",
        )
    )
    state["evidence"] = evidence
    state["trace"] = trace
    return state
