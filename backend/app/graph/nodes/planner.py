from app.core.llm_router import LLMRouter
from app.graph.state import GraphState
from app.schemas.agent import AgentTrace, PlanItem


router = LLMRouter()


def planner_node(state: GraphState) -> GraphState:
    selection = router.select_model("planner")
    plan = [
        PlanItem(
            title="Frame the decision",
            description="Clarify goals, constraints, and success criteria for the request.",
            priority=5,
        ),
        PlanItem(
            title="Research technical options",
            description="Compare viable tools, architecture choices, and implementation tradeoffs.",
            priority=4,
        ),
        PlanItem(
            title="Assess practical risks",
            description="Review delivery speed, cost, and operational complexity.",
            priority=4,
        ),
    ]
    trace = state.get("trace", [])
    trace.append(
        AgentTrace(
            node_name="planner",
            agent_type="planner",
            model_name=selection.model,
            summary="Generated an actionable multi-step research plan.",
        )
    )
    state["plan"] = plan
    state["trace"] = trace
    return state
