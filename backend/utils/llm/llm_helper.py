import pandas as pd
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import add_messages
from typing import Annotated, Tuple


from utils.classes import Situation, Condition
from data.data_loader import load_answers, load_conditions

def find_last_message(message : Annotated[BaseMessage, add_messages]) -> Tuple[BaseMessage, BaseMessage]:
    for i in range(len(message)-1, -1, -1):
        if isinstance(message[i], HumanMessage):
            return message[:i], message[i]
    pass

def answer_concatenation(situation : Situation, condition : Condition) -> str:
    violence_type = situation.violence_type
    answers_df = load_answers()
    answers = "".join(answers_df.loc[violence_type][condition.mask])
    return answers
        