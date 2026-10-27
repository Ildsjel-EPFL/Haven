from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer

from utils.classes import Situation, Condition
from evaluation.evaluation import conditions_evaluation_node, situation_evaluation_node
from utils.llm.llm_state import ChatbotState

workflow = StateGraph(ChatbotState)

workflow.add_node("evaluate_situation", situation_evaluation_node)
workflow.add_node("evaluate_conditions", conditions_evaluation_node)

workflow.add_edge(START, "evaluate_situation")
workflow.add_edge("evaluate_situation", "evaluate_conditions")
workflow.add_edge("evaluate_conditions", END)

graph = workflow.compile(checkpointer=MemorySaver())