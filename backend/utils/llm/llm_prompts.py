situation_evaluation_prompt = """
Tu es un répondant professionnel qui évalue les situations de violence domestique.


"""

condition_evaluation_prompt = """
Tu es un répondant professionnel qui évalue les situations de violence domestique.

La personne a fourni les informations suivantes sur la situation de violence domestique :
{messages}.

Voici les critères qui doivent être pris en compte pour donner les conseils appropriés :
{criteria}.


"""