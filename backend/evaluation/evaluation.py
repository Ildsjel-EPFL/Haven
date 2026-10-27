from langchain_core.prompts import ChatPromptTemplate

from utils.llm.llm_config import llm
from utils.llm.llm_state import ChatbotState
from utils.llm.llm_prompts import situation_evaluation_prompt, condition_evaluation_prompt
from utils.classes import Condition, Situation
from utils.llm.llm_helper import violence_criteria_concatenation, condition_criteria_concatenation

def situation_evaluation_node(state: ChatbotState) -> dict:
    """
    Evaluates the situation based on the provided messages and violence criteria.
    
    Args:
        state (ChatbotState): The current state of the chatbot containing messages and other relevant information
        
    Returns:
        dict: A dictionary containing the evaluation results of the situation."""
    violence_criteria = violence_criteria_concatenation()
    prompt = ChatPromptTemplate.from_template(situation_evaluation_prompt)
    evaluator_llm = llm.with_structured_output(Situation)
    chain  =  prompt | evaluator_llm
    situation = chain.invoke({"messages": state["messages"], "violence_criteria": violence_criteria})
    return {"situation": situation}

def conditions_evaluation_node(state: ChatbotState) -> dict:
    criteria = condition_criteria_concatenation(state["situation"])
    prompt = ChatPromptTemplate.from_template(condition_evaluation_prompt)
    evaluator_llm = llm.with_structured_output(Condition)
    chain  =  prompt | evaluator_llm
    condition = chain.invoke({"messages": state["messages"], "criteria": criteria})
    return {"condition": condition}