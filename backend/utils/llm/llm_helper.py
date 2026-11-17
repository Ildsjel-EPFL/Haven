import pandas as pd
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import add_messages
from typing import Annotated, Tuple
from collections.abc import Sequence

from utils.classes import Condition
from data.data_loader import load_violence_criteria, violence_titles, load_conditions_criteria, load_answers, condition_titles

def find_last_message(message : Annotated[BaseMessage, add_messages]) -> Tuple[BaseMessage, BaseMessage]:
    for i in range(len(message)-1, -1, -1):
        if isinstance(message[i], HumanMessage):
            return message[:i], message[i]
    return None, None

def format_conversation(messages: Sequence[BaseMessage]) -> str:
    formatted = []

    for message in messages:
        if isinstance(message, HumanMessage):
            role = "Utilisateur"
        elif isinstance(message, AIMessage):
            role = "Assistant"
        else:
            role = "Système"

        formatted.append(f"{role} :\n{message.content}")

    return "\n\n".join(formatted)

def violence_criteria_concatenation() -> str:
    """
    Concatenates the violence criteria from the CSV file.
    
    Returns:
        str: The concatenated violence criteria.
    """
    violence_criteria = load_violence_criteria()
    violence_text = ""
    for title, criterion in zip(violence_titles, violence_criteria["Critères"]):
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
    print(f"Concatenated conditions for violence type '{violence}' done.")
    return condition_text.rstrip()

def condition_answer_concatenation(violence: str, condition: Condition) -> str:
    """
    Concatenates the answers based on the situation and condition provided.
    
    Args:
        violence: The violence code used to select the correct answers.
        condition: The evaluated conditions for that violence.

    Returns:
        str: The concatenated answers.
    """
    answers_df = load_answers()
    return "\n\n".join(
        f"## {action}:\n{answer}"
        for action, enabled, answer in zip(
            condition_titles,
            condition.mask,
            answers_df.loc[violence],
        )
        if enabled
    )