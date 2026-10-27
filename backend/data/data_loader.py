import pandas as pd

def load_violence_criteria() -> pd.DataFrame:
    """
    Load the violence criteria from the CSV file and return a DataFrame.
    """
    return pd.read_csv(r"data\violence_criteria.csv", index_col=0, encoding="utf-8-sig")

def load_conditions_criteria() -> pd.DataFrame:
    """
    Load the conditions from the CSV file and return a DataFrame.
    """
    return pd.read_csv(r"data\conditions.csv", index_col=0, encoding="utf-8-sig")

def load_answers() -> pd.DataFrame:
    """
    Load the answers from the CSV file and return a DataFrame.
    """
    return pd.read_csv(r"data\answers.csv", index_col=0, encoding="utf-8-sig")

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
    "Protéger les avoirs"]