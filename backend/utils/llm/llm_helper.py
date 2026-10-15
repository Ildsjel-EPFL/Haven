from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import add_messages
from typing import Annotated, Tuple

def find_last_message(message : Annotated[BaseMessage, add_messages]) -> Tuple[BaseMessage, BaseMessage]:
    for i in range(len(message)-1, -1, -1):
        if isinstance(message[i], HumanMessage):
            return message[:i], message[i]
    pass