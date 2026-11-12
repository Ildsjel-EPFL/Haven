from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate

from evaluation.evaluation import evaluate_conditions_for_violence
from utils.classes import Situation
from utils.llm.llm_config import llm
from utils.llm.llm_helper import condition_answer_concatenation
from utils.llm.llm_prompts import (
    clarification_response_prompt,
    conflict_response_prompt,
    violence_response_prompt,
)
from utils.llm.llm_state import ChatbotState


def _response_update(state: ChatbotState, content: str, questions: list[str]) -> dict:
    return {
        "response": content,
        "messages": [AIMessage(content=content)],
        "pending_questions": questions,
    }


def clarification_response_node(state: ChatbotState) -> dict:
    prompt = ChatPromptTemplate.from_template(clarification_response_prompt)
    response = (prompt | llm).invoke(
        {
            "messages": state["messages"],
            "reason": state.get("clarification_reason", ""),
            "language": state["language"],
        }
    )
    return _response_update(state, response.content, ["clarification"])


def conflict_response_node(state: ChatbotState) -> dict:
    prompt = ChatPromptTemplate.from_template(conflict_response_prompt)
    response = (prompt | llm).invoke(
        {
            "messages": state["messages"],
            "language": state["language"],
        }
    )
    return _response_update(state, response.content, [])


def evaluate_conditions_and_answers_node(state: ChatbotState) -> dict:
    situation: Situation = state["situation"]
    conditions = {}
    answers = {}

    for violence in situation.violence_types:
        condition = evaluate_conditions_for_violence(violence, state)
        conditions[violence] = condition
        answers[violence] = condition_answer_concatenation(violence, condition)

    return {"conditions": conditions, "answers": answers}


def violence_response_node(state: ChatbotState) -> dict:
    prompt = ChatPromptTemplate.from_template(violence_response_prompt)
    response = (prompt | llm).invoke(
        {
            "messages": state["messages"],
            "answers": "\n\n".join(state.get("answers", {}).values()),
            "unknown_topics": _unknown_topics(state["situation"]),
            "language": state["language"],
        }
    )
    return _response_update(
        state,
        response.content,
        _unknown_topics(state["situation"]),
    )


def _unknown_topics(situation: Situation) -> list[str]:
    topics = []
    if situation.children_involved is None:
        topics.append("children involved")
    return topics
