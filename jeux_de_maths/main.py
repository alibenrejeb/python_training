import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    operateur_str = "+"
    calcul = a + b
    if o == 1:
        operateur_str = "*"
        calcul = a * b
    reponse_str = input(f"Calculez {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)

    return reponse_int == calcul


nb_points = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS}:")
    if poser_question():
        nb_points += 1
        print("Réponse correct")
    else:
        print("Réponse incorrecte")
    print()

print(f"Votre note est : {nb_points}/{NB_QUESTIONS}")
moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS:
    print("Excellent!")
elif nb_points == 0:
    print("Révisez vos maths!")
elif nb_points < moyenne:
    print("Peut mieux faire")
else:
    print("Pas mal")
