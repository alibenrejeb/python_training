def afficher_table_multiplication(n: int, v_min: int = 1, v_maw: int = 10):
    if v_min > v_maw:
        print("ERROR: v_maw must be greater than or equal to v_min")
        return
    for i in range(v_min, v_maw + 1):
        print(f"{i} x {n} = {n*i}")


def poser_une_question(question: str, reponses, reponse: str):
    global score
    print(question)
    char = ord("a")
    for rep in reponses:
        print(f"({chr(char)}) {rep}")
        char += 1
    if input("Votre réponse: ") == reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")


score = 0
"""poser_une_question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Lyon"), "c")
poser_une_question("Quelle est la capitale de l'Italy ?", ("Rome", "Florence", "Milan", "Venis"), "a")

print(f"Votre score final: {score}")"""

# Fonction Callback


def multiplicaiton(a, b):
    return a * b


def afficher_table(n, operateur, operation_cb):
    for i in range(1, 10):
        print(f"{i} {operateur} {n} = {operation_cb(i, n)}")


afficher_table(2, "X", multiplicaiton)
print()
print("Utilisation de la fonction lambda :")
afficher_table(2, "X", lambda a, b: a + b)
print()
afficher_table(2, "X", lambda a, b: a ** b)
print()
# Nombre variable de parameteres


def somme1(titre, *args):
    print("Titre :", titre, end=" ", flush=False)
    v_sum = 0
    for n in args:
        v_sum += n
    return v_sum


def somme2(titre, **args):
    print("Titre :", titre, end=" ", flush=False)
    v_sum = 0
    for n in args.values():
        v_sum += n
    return v_sum


print(somme1("Somme des notes: ", 12, 10, 9))
print(somme2("Somme des notes: ", maths=18, geo=12, anglais=15))
