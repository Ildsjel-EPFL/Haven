from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer

from evaluation.evaluation import classify_situation_node
from response.response import (
    clarification_response_node,
    conflict_response_node,
    evaluate_conditions_and_answers_node,
    general_response_node,
    violence_response_node,
)
from utils.llm.llm_state import ChatbotState
from utils.classes import Condition, Situation


def route_after_classification(state: ChatbotState) -> str:
    situation = state["situation"]

    if situation.needs_clarification:
        return "clarification"
    if situation.violence_types:
        return "conditions"
    if situation.conflict is True:
        return "conflict"
    return "general"


def build_graph() -> CompiledStateGraph:
    workflow = StateGraph(ChatbotState)

    workflow.add_node("classify_situation", classify_situation_node)
    workflow.add_node("evaluate_conditions", evaluate_conditions_and_answers_node)
    workflow.add_node("violence_response", violence_response_node)
    workflow.add_node("conflict_response", conflict_response_node)
    workflow.add_node("clarification_response", clarification_response_node)
    workflow.add_node("general_response", general_response_node)

    workflow.add_edge(START, "classify_situation")
    workflow.add_conditional_edges(
        "classify_situation",
        route_after_classification,
        {
            "clarification": "clarification_response",
            "conflict": "conflict_response",
            "conditions": "evaluate_conditions",
            "general": "general_response",
        },
    )
    workflow.add_edge("evaluate_conditions", "violence_response")
    workflow.add_edge("violence_response", END)
    workflow.add_edge("conflict_response", END)
    workflow.add_edge("clarification_response", END)
    workflow.add_edge("general_response", END)

    allowed_types = (
        Condition,
        Situation,
        f"{Condition.__module__}.{Condition.__qualname__}",
        f"{Situation.__module__}.{Situation.__qualname__}",
    )
    serde = JsonPlusSerializer(allowed_msgpack_modules=allowed_types)

    # A checkpointer is required for the `interrupt` feature to save state
    memory = MemorySaver(serde=serde)

    return workflow.compile(checkpointer=memory)


graph: CompiledStateGraph = build_graph()
