from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer
from langgraph.graph.state import CompiledStateGraph

from utils.classes import Situation, Condition
from evaluation.evaluation import conditions_evaluation_node, situation_evaluation_node
from response.response import response_generation_node
from utils.llm.llm_state import ChatbotState

def build_graph() -> CompiledStateGraph[ChatbotState, None, ChatbotState, ChatbotState]:
    """
    Builds and compiles the state graph for the chatbot workflow.
    
    Returns:
        CompiledStateGraph[ChatbotState, None, ChatbotState, ChatbotState]: The compiled state graph representing the chatbot workflow.
    """
    workflow = StateGraph(ChatbotState)

    workflow.add_node("evaluate_situation", situation_evaluation_node)
    workflow.add_node("evaluate_conditions", conditions_evaluation_node)
    workflow.add_node("generate_response", response_generation_node)

    workflow.add_edge(START, "evaluate_situation")
    workflow.add_edge("evaluate_situation", "evaluate_conditions")
    workflow.add_edge("evaluate_conditions", "generate_response")
    workflow.add_edge("generate_response", END)

    return workflow.compile(checkpointer=MemorySaver())

graph : CompiledStateGraph[ChatbotState, None, ChatbotState, ChatbotState] = build_graph()