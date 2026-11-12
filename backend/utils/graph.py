from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from evaluation.evaluation import classify_situation_node
from response.response import (
    clarification_response_node,
    conflict_response_node,
    evaluate_conditions_and_answers_node,
    violence_response_node,
)
from utils.llm.llm_state import ChatbotState


def route_after_classification(state: ChatbotState) -> str:
    situation = state["situation"]

    if state.get("needs_clarification", False):
        return "clarification"
    if not situation.violence_types:
        return "conflict" if situation.conflict is True else "clarification"
    return "conditions"


def build_graph() -> CompiledStateGraph:
    workflow = StateGraph(ChatbotState)

    workflow.add_node("classify_situation", classify_situation_node)
    workflow.add_node("evaluate_conditions", evaluate_conditions_and_answers_node)
    workflow.add_node("violence_response", violence_response_node)
    workflow.add_node("conflict_response", conflict_response_node)
    workflow.add_node("clarification_response", clarification_response_node)

    workflow.add_edge(START, "classify_situation")
    workflow.add_conditional_edges(
        "classify_situation",
        route_after_classification,
        {
            "clarification": "clarification_response",
            "conflict": "conflict_response",
            "conditions": "evaluate_conditions",
        },
    )
    workflow.add_edge("evaluate_conditions", "violence_response")
    workflow.add_edge("violence_response", END)
    workflow.add_edge("conflict_response", END)
    workflow.add_edge("clarification_response", END)

    return workflow.compile(checkpointer=MemorySaver())


graph: CompiledStateGraph = build_graph()
