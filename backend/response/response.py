from langchain_core.prompts import ChatPromptTemplate

from utils.llm.llm_config import llm
from utils.llm.llm_state import ChatbotState
from utils.classes import Condition, Situation
from utils.llm.llm_helper import condition_answer_concatenation

def response_generation_node(state: ChatbotState) -> dict:
    """
    Generates a response based on the provided messages, situation, and condition.
    
    Args:
        state (ChatbotState): The current state of the chatbot containing messages, situation, and condition.

    Returns:
        dict: A dictionary containing the generated response.
    """
    answers = condition_answer_concatenation(state["situation"], state["condition"])
    prompt = ChatPromptTemplate.from_template(answers)
    response_llm = llm
    chain  =  prompt | response_llm
    response = chain.invoke({"messages": state["messages"]})
    return {"response": response}