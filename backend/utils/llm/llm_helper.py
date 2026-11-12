import pandas as pd
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import add_messages
from typing import Annotated, Tuple

from utils.classes import Situation, Condition
from data.data_loader import load_violence_criteria, violence_titles, load_conditions_criteria, load_answers, condition_titles

def find_last_message(message : Annotated[BaseMessage, add_messages]) -> Tuple[BaseMessage, BaseMessage]:
    for i in range(len(message)-1, -1, -1):
        if isinstance(message[i], HumanMessage):
            return message[:i], message[i]
    return None, None

def violence_criteria_concatenation() -> str:
    """
    Concatenates the violence criteria from the CSV file.
    
    Returns:
        str: The concatenated violence criteria.
    """
    violence_criteria = load_violence_criteria()
    violence_text = ""
    for title, criterion in zip(violence_titles, violence_criteria["criteria"]):
        violence_text += f"## {title}:\n{criterion}\n\n"
    return violence_text.rstrip()

def condition_criteria_concatenation(violence : str) -> str:
    """
    Concatenates the conditions based on the situation and condition provided.

    Args:
        violence (str): The type of violence to concatenate conditions for.

    Returns:
        str: The concatenated conditions.
    """
    conditions_criteria = load_conditions_criteria()
    condition_text = ""
    for action, cond in zip(condition_titles, conditions_criteria.loc[violence]):
        if cond:
            condition_text += f"## {action}:\n{cond}\n\n"
    return condition_text.rstrip()

def condition_answer_concatenation(situation : Situation, condition : Condition) -> str:
    """
    Concatenates the answers based on the situation and condition provided.
    
    Args:
        situation (Situation): An instance of the Situation class representing the current situation.
        condition (Condition): An instance of the Condition class representing the current condition.

    Returns:
        str: The concatenated answers.
    """
    answers = ""
    violence_type = situation.violence_type
    answers_df = load_answers()
    validated_condition_titles = [action for action, cond in zip(condition_titles, condition.mask) if cond]
    for action, cond in zip(validated_condition_titles, answers_df.loc[violence_type][condition.mask]):
        if cond:
            answers += f"## {action}:\n{cond}\n\n"
    return answers.rstrip()        