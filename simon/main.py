import random
import time
import os

"""
- Longueur séquence initiale: 4
- Durée de mémorisation: 3s
- A chaque tour ajouter: 1 chiffre
- Un nombre d'essais

Facile
    longueur_sec_initiale: 3
    duree_memorisation: 4
    increment_sequence: 1
    nombre_essais: 2
Normal
    longueur_sec_initiale: 4
    duree_memorisation: 3
    increment_sequence: 1
    nombre_essais: 1
Difficile
    longueur_sec_initiale: 4
    duree_memorisation: 2
    increment_sequence: 2
    nombre_essais: 0
"""

NIVEAUX_DIFFICULTE = (
    {
        "titre": "Facile",
        "longueur_sec_initiale": 3,
        "duree_memorisation_sec": 4,
        "increment_sequence": 1,
        "nombre_essais": 3
    },
    {
        "titre": "Normal",
        "longueur_sec_initiale": 4,
        "duree_memorisation_sec": 3,
        "increment_sequence": 1,
        "nombre_essais": 2
    },
    {
        "titre": "Difficile",
        "longueur_sec_initiale": 4,
        "duree_memorisation_sec": 2,
        "increment_sequence": 2,
        "nombre_essais": 1
    }
)


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def genere_sequence(n):
    seq = ""
    for i in range(n):
        seq += str(random.randint(0, 9))
    return seq


def choix_menu(v_min, v_max):
    choice_str = input(f"Donnez une valeur entre {v_min} et {v_max}: ")
    try:
        choice_int = int(choice_str)
    except:
        print("ERREUR: vous devez choisir une valeur numérique")
        return choix_menu(v_min, v_max)
    if not (v_min <= choice_int <= v_max):
        print(f"ERREUR: vous devez choisir une valeur entre {v_min} et {v_max}")
        return choix_menu(v_min, v_max)
    return choice_int


def choix_niveau_difficulte(niveau_difficulte):
    print("Choissiez votre niveau")
    index = 1
    for niveau in niveau_difficulte:
        print(f"{index} - {niveau['titre']}")
        index += 1
    choice = choix_menu(1, len(niveau_difficulte))
    return niveau_difficulte[choice - 1]


# Choisir niveau de difficulté
niveau_difficulte_dict = choix_niveau_difficulte(NIVEAUX_DIFFICULTE)

score = 0
sequence = genere_sequence(niveau_difficulte_dict["longueur_sec_initiale"])
nombre_essais_restants = niveau_difficulte_dict["nombre_essais"]

clear_screen()
print(f"Début du jeu - niveau {niveau_difficulte_dict['titre']}")

while True:
    print("Retenez la séquence")
    time.sleep(1)
    print(f"{sequence}")
    time.sleep(niveau_difficulte_dict["duree_memorisation_sec"])
    clear_screen()

    print(f"Nombre d'essais restants: {nombre_essais_restants}")
    print(f"Votre score: {score}")
    reponse = input("Votre réponse: ")
    if reponse == sequence:
        score += 1
        sequence += genere_sequence(niveau_difficulte_dict["increment_sequence"])
        time.sleep(1)
        clear_screen()
    else:
        nombre_essais_restants -= 1
        if nombre_essais_restants < 0:
            break
        print("Mauvaise réponse. réessayez.")
    time.sleep(1)
    clear_screen()

print(f"Mauvaise réponse, la séquence était: {sequence}")
print(f"Votre score final: {score}")
