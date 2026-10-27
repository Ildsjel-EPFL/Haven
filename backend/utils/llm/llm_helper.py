import pandas as pd
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import add_messages
from typing import Annotated, Tuple


from utils.classes import Situation, Condition
from data.data_loader import load_answers, load_conditions, condition_titles

def find_last_message(message : Annotated[BaseMessage, add_messages]) -> Tuple[BaseMessage, BaseMessage]:
    for i in range(len(message)-1, -1, -1):
        if isinstance(message[i], HumanMessage):
            return message[:i], message[i]
    pass

def condition_concatenation(situation : Situation) -> str:
    """
    Concatenates the conditions based on the situation and condition provided.

    Args:
        situation (Situation): An instance of the Situation class representing the current situation.

    Returns:
        str: The concatenated conditions.
    """
    conditions_df = load_conditions()
    condition_text = ""
    for action, cond in zip(condition_titles, conditions_df.loc[situation.violence_type]):
        if cond:
            condition_text += f"## {action}:\n{cond}\n\n"
    return condition_text.rstrip()

def answer_concatenation(situation : Situation, condition : Condition) -> str:
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
        