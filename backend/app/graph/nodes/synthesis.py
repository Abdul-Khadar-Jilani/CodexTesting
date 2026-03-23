from app.core.llm_router import LLMRouter
from app.graph.state import GraphState
from app.schemas.agent import AgentTrace, FinalMemo, MemoSection


router = LLMRouter()


def synthesis_node(state: GraphState) -> GraphState:
    selection = router.select_model("synthesis")
    memo = FinalMemo(
        executive_summary="DecisionGraph turns complex questions into structured, inspectable research workflows.",
        recommendation="Use FastAPI, Supabase, Groq, and Gemini in a multi-model workflow with persistent run history.",
        confidence_score=0.84,
        sections=[
            MemoSection(
                heading="Architecture",
                content="FastAPI handles APIs and orchestration, while Supabase persists tasks, runs, and evidence.",
            ),
            MemoSection(
                heading="Model Strategy",
                content="Groq handles rapid structured steps, and Gemini is reserved for long-form synthesis.",
            ),
        ],
    )
    trace = state.get("trace", [])
    trace.append(
        AgentTrace(
            node_name="synthesis",
            agent_type="synthesis",
            model_name=selection.model,
            summary="Produced the final recommendation memo.",
        )
    )
    state["memo"] = memo
    state["trace"] = trace
    return state
