# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions


def demander_reponse_numerique_utilisateur(v_min, v_max):
    reponse_str = input("Votre réponse (entre " + str(v_min) + " et " + str(v_max) + "): ")
    try:
        v_int = int(reponse_str)
        if v_min <= v_int <= v_max:
            return v_int
        print(f"ERREUR : Vous devez rentrer un nombre entre {v_min} et {v_max}")
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utilisateur(v_min, v_max)


def poser_question(question):
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION")
    print("  " + question[0])
    for i in range(len(choix)):
        print(f"({i + 1})", choix[i])
    print()
    reponse_int = demander_reponse_numerique_utilisateur(1, len(choix))

    if choix[reponse_int - 1].upper() == bonne_reponse.upper():
        print("Bonne réponse")
        print()
        return True

    print("Mauvaise réponse")
    print()
    return False


def lancer_questionnaire(v_questionnaire):
    score = 0
    for question in v_questionnaire:
        if poser_question(question):
            score += 1
    print(f"Score final : {score} sur {len(v_questionnaire)}")


'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"),
    ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
)
lancer_questionnaire(questionnaire)
