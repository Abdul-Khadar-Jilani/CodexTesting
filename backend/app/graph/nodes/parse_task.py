from app.core.llm_router import LLMRouter
from app.graph.state import GraphState
from app.schemas.agent import AgentTrace


router = LLMRouter()


def parse_task_node(state: GraphState) -> GraphState:
    selection = router.select_model("parse")
    trace = state.get("trace", [])
    trace.append(
        AgentTrace(
            node_name="parse_task",
            agent_type="system",
            model_name=selection.model,
            summary="Parsed task into workflow-ready research inputs.",
        )
    )
    state["trace"] = trace
    return state
