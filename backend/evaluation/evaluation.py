from langchain_core.prompts import ChatPromptTemplate

from utils.llm.llm_config import llm
from utils.llm.llm_state import ChatbotState
from utils.llm.llm_prompts import situation_evaluation_prompt, condition_evaluation_prompt
from utils.classes import Condition, Situation
from utils.llm.llm_helper import violence_criteria_concatenation, condition_criteria_concatenation

def classify_situation_node(state: ChatbotState) -> dict:
    """
    Classifies the complete conversation, including answers to follow-up questions.
    """
    prompt = ChatPromptTemplate.from_template(situation_evaluation_prompt)
    evaluator_llm = llm.with_structured_output(Situation)
    situation = (prompt | evaluator_llm).invoke(
        {
            "messages": state["messages"],
            "previous_evaluation": state.get("situation"),
            "pending_questions": state.get("pending_questions", []),
            "violence_criteria": violence_criteria_concatenation(),
        }
    )
    return {
        "situation": situation,
        "needs_clarification": situation.needs_clarification,
        "clarification_reason": situation.clarification_reason,
    }

def evaluate_conditions_for_violence(
    violence: str,
    state: ChatbotState,
) -> Condition:
    """
    Evaluates all applicable actions for one violence type.
    """
    prompt = ChatPromptTemplate.from_template(condition_evaluation_prompt)
    evaluator_llm = llm.with_structured_output(Condition)
    return (prompt | evaluator_llm).invoke(
        {
            "messages": state["messages"],
            "criteria": condition_criteria_concatenation(violence),
        }
    )


def evaluate_conditions_node(state: ChatbotState) -> dict:
    conditions = {}
    for violence in state["situation"].violence_types:
        conditions[violence] = evaluate_conditions_for_violence(violence, state)
    return {"conditions": conditions}
