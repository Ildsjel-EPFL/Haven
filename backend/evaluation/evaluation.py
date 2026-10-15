from langchain_core.prompts import ChatPromptTemplate
from utils.llm.llm_config import llm
from utils.llm.llm_state import ChatbotState
from utils.llm.llm_prompts import situation_evaluation_prompt
from utils.classes import Situation

def situation_evaluation_node(state: ChatbotState) -> Situation:
    prompt = ChatPromptTemplate.from_template(situation_evaluation_prompt)
    evaluator_llm = llm.with_structured_output(Situation)
    chain  =  prompt | evaluator_llm
    return chain.invoke(state["messages"])