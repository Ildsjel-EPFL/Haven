import pandas as pd

path = r"data\Transformative Project - "

def load_violence_criteria() -> pd.DataFrame:
    """
    Load the violence criteria from the CSV file and return a DataFrame.
    """
    path_conditions_violences = path + "Conditions Violences.csv"
    return pd.read_csv(path_conditions_violences, index_col=0, encoding="utf-8-sig")

def load_conditions_criteria() -> pd.DataFrame:
    """
    Load the conditions from the CSV file and return a DataFrame.
    """
    path_conditions_actions = path + "Conditions Actions.csv"
    return pd.read_csv(path_conditions_actions, index_col=0, encoding="utf-8-sig")

def load_answers() -> pd.DataFrame:
    """
    Load the answers from the CSV file and return a DataFrame.
    """
    path_reponses = path + "Réponses.csv"
    return pd.read_csv(path_reponses, index_col=0, encoding="utf-8-sig")

violence_titles = ["Violence physique", "Violence sexuelle", "Violence psychologique", "Violence économique"]

condition_titles = [
    "Appeler la police (117)",
    "Préparer un sac",
    "Quitter le domicile",
    "Rassembler les documents importants",
    "Préserver les preuves",
    "Constat médical",
    "Consultation et groupes de parole",
    "Parler à une personne de confiance",
    "Appeler le numéro pour l'aide aux victimes en Suisse (142)",
    "Soutien financier, juridique et psychologique",
    "Protéger ses avoirs",
    "Reconnaître les humiliations et les dévalorisations",
    "Quand l'autre vous fait douter de ce que vous vivez",
    "Quand l'autre vous rend responsable de ses comportements",
    "Retrouver du soutien face à l'isolement",
    "Reconnaître le contrôle de votre quotidien",
    "Protéger vos échanges et votre vie privée numérique",
    "Faire face aux intimidations et aux menaces",
    "Quand les menaces concernent les enfants",
    "Faire face au harcèlement et aux contacts imposés",
    "Quand l'autre menace de se suicider ou de se faire du mal",
    "Quand l'autre menace de révéler des informations privées"
    ]