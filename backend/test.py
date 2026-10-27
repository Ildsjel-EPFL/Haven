# import os
# from dotenv import load_dotenv

# load_dotenv()

# RCP_api_key = os.getenv("RCP_API_KEY")
# print(f"RCP_api_key: {RCP_api_key}")    # Does work, prints the value of RCP_API_KEY from .env file





# from utils.classes import Condition
# from data.data_loader import load_answers

# cond = Condition(
#     police=True,
#     pack_your_things=False,
#     leave_home=True,
#     gather_docs=True,
#     preserve_evidence=False,
#     medical_report=True,
#     counselling_support_group=False,
#     neighbour=False,
#     lavi=False,
#     fin_legal_psy_support=True,
#     assets_protection=False
# )

# df = load_answers()
# print("".join(df.loc["PHY"][cond.mask])) # Does work if in the backend directory, prints the answers corresponding to the mask of the Condition object for PHY violence type




from data.data_loader import load_conditions, condition_titles, load_answers
from utils.classes import Situation, Condition

situation = Situation(
    security_emergency=False,
    health_emergency=False,
    conflict=False,
    physical_violence=True,
    sexual_violence=False,
    psychological_violence=False,
    economical_violence=False,
    residential_permit=False,
    children_involved=False,
    forced_marriage=False
)

condition = Condition(
    police=True,
    pack_your_things=False,
    leave_home=True,
    gather_docs=True,
    preserve_evidence=False,
    medical_report=True,
    counselling_support_group=False,
    neighbour=False,
    lavi=False,
    fin_legal_psy_support=True,
    assets_protection=False
)

conditions_df = load_conditions()
answers = ""
violence_type = situation.violence_type
answers_df = load_answers()
validated_condition_titles = [action for action, cond in zip(condition_titles, condition.mask) if cond]
for action, cond in zip(validated_condition_titles, answers_df.loc[violence_type][condition.mask]):
    if cond:
        answers += f"## {action}:\n{cond}\n\n"
print(answers.rstrip())