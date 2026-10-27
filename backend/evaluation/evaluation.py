from langchain_core.prompts import ChatPromptTemplate

from utils.llm.llm_config import llm
from utils.llm.llm_state import ChatbotState
from utils.llm.llm_prompts import situation_evaluation_prompt
from utils.classes import Condition, Situation
from utils.llm.llm_helper import condition_criteria_concatenation

def situation_evaluation_node(state: ChatbotState) -> Situation:
    prompt = ChatPromptTemplate.from_template(situation_evaluation_prompt)
    evaluator_llm = llm.with_structured_output(Situation)
    chain  =  prompt | evaluator_llm
    return chain.invoke(state["messages"])

def conditions_evaluation_node(state: ChatbotState) -> Condition:
    criteria = condition_criteria_concatenation(state["situation"])
    prompt = ChatPromptTemplate.from_template(situation_evaluation_prompt)
    evaluator_llm = llm.with_structured_output(Condition)
    chain  =  prompt | evaluator_llm
    return chain.invoke({"messages": state["messages"], "criteria": criteria})