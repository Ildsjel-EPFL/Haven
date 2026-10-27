from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

from utils.classes import Situation

class ChatbotState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    situation_eval : Situation
    language : str = "fr"