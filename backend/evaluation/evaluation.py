from time import perf_counter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig

from utils.llm.llm_config import llm
from utils.llm.llm_state import ChatbotState
from utils.llm.llm_prompts import situation_evaluation_prompt, condition_evaluation_prompt
from utils.classes import Condition, Situation
from utils.llm.llm_helper import violence_criteria_concatenation, condition_criteria_concatenation, format_conversation

# from time import perf_counter

MAX_CLARIFICATION_ATTEMPTS = 2


def classify_situation_node(
    state: ChatbotState,
    config: RunnableConfig,
) -> dict:
    """
    Classifies the complete conversation, including answers to follow-up questions.
    """
    print(f"Classify situation node invoked. Current state: {state}")
    prompt = ChatPromptTemplate.from_template(situation_evaluation_prompt)
    evaluator_llm = llm.with_structured_output(Situation)
    situation = (prompt | evaluator_llm).invoke(
        {
            "messages": format_conversation(state["messages"]),
            "previous_evaluation": state.get("situation"),
            "pending_questions": state.get("pending_questions", []),
            "violence_criteria": violence_criteria_concatenation(),
        }
    )
    thread_id = config["configurable"]["thread_id"]
    clarification_attempts = state.get("clarification_attempts", 0)
    if situation.needs_clarification:
        clarification_attempts += 1
        if clarification_attempts > MAX_CLARIFICATION_ATTEMPTS:
            situation = situation.model_copy(
                update={
                    "needs_clarification": False,
                    "clarification_reason": None,
                }
            )
    else:
        clarification_attempts = 0
    print(f"Thread ID: {thread_id}: Situation classified: {situation}")
    return {
        "situation": situation,
        "needs_clarification": situation.needs_clarification,
        "clarification_reason": situation.clarification_reason,
        "clarification_attempts": clarification_attempts,
    }

def evaluate_conditions_for_violence(
    violence: str,
    state: ChatbotState,
    thread_id: str,
) -> Condition:
    """
    Evaluates all applicable actions for one violence type.
    """
    prompt = ChatPromptTemplate.from_template(condition_evaluation_prompt)
    evaluator_llm = llm.with_structured_output(Condition)
    print(f"Thread ID: {thread_id}: Evaluating conditions for violence type: {violence}")
    
    # start = perf_counter()
    criteria = condition_criteria_concatenation(violence)
    # print("criteria:", perf_counter() - start)
    
    # start = perf_counter()
    response = (prompt | evaluator_llm).invoke({
        "messages": format_conversation(state["messages"]),
        "criteria": criteria,
    })
    # print("LLM:", perf_counter() - start)
    # criteria = condition_criteria_concatenation(violence)
    # print("Messages: ", state["messages"])
    # response = (prompt | evaluator_llm).invoke(
    #     {"messages": state["messages"],
    #                 "criteria": criteria,
    #             }
    #         )
    print(f"Thread ID: {thread_id}: Conditions evaluated for violence type '{violence}': {response}")
    return response

def evaluate_conditions_node(
    state: ChatbotState,
    config: RunnableConfig,
) -> dict:
    print(f"Evaluate conditions node invoked. Situation violence types: {state['situation'].violence_types}")
    thread_id = config["configurable"]["thread_id"]
    conditions = {}
    for violence in state["situation"].violence_types:
        conditions[violence] = evaluate_conditions_for_violence(
            violence,
            state,
            thread_id,
        )
    print(f"Thread ID: {thread_id}: Conditions evaluated for violence types: {list(conditions.keys())}")
    return {"conditions": conditions}
