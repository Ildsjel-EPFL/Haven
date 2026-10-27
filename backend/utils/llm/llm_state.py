from typing import Annotated, Sequence, TypedDict, NotRequired
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

from utils.classes import Situation, Condition

class ChatbotState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    situation : NotRequired[list[Situation]]
    condition : NotRequired[list[Condition]]
    language : str = "fr"