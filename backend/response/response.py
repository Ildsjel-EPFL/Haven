from langchain_core.prompts import ChatPromptTemplate

from utils.llm.llm_config import llm
from utils.llm.llm_state import ChatbotState
from utils.classes import Condition, Situation
from utils.llm.llm_prompts import first_response_prompt
from utils.llm.llm_helper import condition_answer_concatenation
from evaluation.evaluation import first_round_situation_eval, first_round_conditions_eval

def response_generation_node(state: ChatbotState) -> dict:
    """
    Generates a response based on the provided messages, situation, and condition.
    
    Args:
        state (ChatbotState): The current state of the chatbot containing messages, situation, and condition.

    Returns:
        dict: A dictionary containing the generated response.
    """
    answers = condition_answer_concatenation(
        state["situation"],
        state["condition"],
    )

    prompt = ChatPromptTemplate.from_template(first_response_prompt)
    chain = prompt | llm

    response = chain.invoke(
        {
            "messages": state["messages"],
            "answers": answers,
            "language": state["language"],
        }
    )

    return {"response": response.content}


def get_first_round_violence_response_node(state: ChatbotState) -> dict:
    situation : Situation = first_round_situation_eval(state)
    answers : str = ""
    for violence in situation.violence_types:
        condition : Condition = first_round_conditions_eval(violence, state)
        specific_answers : str = condition_answer_concatenation(situation, condition)
        answers += specific_answers + "\n"
    prompt = ChatPromptTemplate.from_template(first_response_prompt)
    chain = prompt | llm

    response = chain.invoke(
        {
            "messages": state["messages"],
            "answers": answers,
            "language": state["language"],
        }
    )

    return {"response": response.content}