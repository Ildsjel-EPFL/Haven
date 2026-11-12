from typing import Annotated, NotRequired, Sequence, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

from utils.classes import Condition, Situation

class ChatbotState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    language: str

    situation: NotRequired[Situation]
    needs_clarification: NotRequired[bool]
    clarification_reason: NotRequired[str | None]
    pending_questions: NotRequired[list[str]]

    conditions: NotRequired[dict[str, Condition]]
    answers: NotRequired[dict[str, str]]
    response: NotRequired[str]