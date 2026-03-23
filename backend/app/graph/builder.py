from app.graph.nodes.critic import critic_node
from app.graph.nodes.parse_task import parse_task_node
from app.graph.nodes.planner import planner_node
from app.graph.nodes.research import research_node
from app.graph.nodes.synthesis import synthesis_node
from app.graph.state import GraphState


def execute_workflow(initial_state: GraphState) -> GraphState:
    state = parse_task_node(initial_state)
    state = planner_node(state)
    state = research_node(state)
    state = critic_node(state)
    state = synthesis_node(state)
    return state
