from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig

from evaluation.evaluation import evaluate_conditions_for_violence
from utils.classes import Situation
from utils.llm.llm_config import llm
from utils.llm.llm_helper import condition_answer_concatenation, format_conversation
from utils.llm.llm_prompts import (
    clarification_response_prompt,
    conflict_response_prompt,
    general_response_prompt,
    violence_response_prompt,
)
from utils.llm.llm_state import ChatbotState


def _response_update(state: ChatbotState, content: str, questions: list[str]) -> dict:
    return {
        "response": content,
        "messages": [AIMessage(content=content)],
        "pending_questions": questions,
        "clarification_attempts": state.get("clarification_attempts", 0)
        if questions
        else 0,
    }


def clarification_response_node(state: ChatbotState) -> dict:
    print(f"Clarification response node invoked. Needs clarification: {state.get('needs_clarification', False)}")
    prompt = ChatPromptTemplate.from_template(clarification_response_prompt)
    response = (prompt | llm).invoke(
        {
            "messages": format_conversation(state["messages"]),
            "reason": state.get("clarification_reason", ""),
            "language": state["language"],
        }
    )
    print(f"Clarification response generated: {response.content}")
    return _response_update(state, response.content, ["clarification"])


def conflict_response_node(state: ChatbotState) -> dict:
    print(f"Conflict response node invoked. Situation conflict: {state['situation'].conflict}")
    prompt = ChatPromptTemplate.from_template(conflict_response_prompt)
    response = (prompt | llm).invoke(
        {
            "messages": format_conversation(state["messages"]),
            "language": state["language"],
        }
    )
    print(f"Conflict response generated: {response.content}")
    return _response_update(state, response.content, [])


def general_response_node(state: ChatbotState) -> dict:
    prompt = ChatPromptTemplate.from_template(general_response_prompt)
    response = (prompt | llm).invoke(
        {
            "messages": format_conversation(state["messages"]),
            "language": state["language"],
        }
    )
    print(f"General response generated: {response.content}")
    return _response_update(state, response.content, [])


def evaluate_conditions_and_answers_node(
    state: ChatbotState,
    config: RunnableConfig,
) -> dict:
    print(f"Evaluate conditions and answers node invoked. Situation violence types: {state['situation'].violence_types}")
    thread_id = config["configurable"]["thread_id"]
    situation: Situation = state["situation"]
    conditions = {}
    answers = {}

    for violence in situation.violence_types:
        condition = evaluate_conditions_for_violence(violence, state, thread_id)
        conditions[violence] = condition
        answers[violence] = condition_answer_concatenation(violence, condition)
    print(f"Thread ID: {thread_id}: Conditions and answers evaluated for violence types: {situation.violence_types}")
    return {"conditions": conditions, "answers": answers}


def violence_response_node(state: ChatbotState) -> dict:
    print(f"Violence response node invoked. Situation violence types: {state['situation'].violence_types}")
    prompt = ChatPromptTemplate.from_template(violence_response_prompt)
    response = (prompt | llm).invoke(
        {
            "messages": format_conversation(state["messages"]),
            "answers": "\n\n".join(state.get("answers", {}).values()),
            "unknown_topics": _unknown_topics(state["situation"]),
            "language": state["language"],
        }
    )
    print(f"Violence response generated: {response.content}")
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
