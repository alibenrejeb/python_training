"""
1 pouce = 2.54 cm
1 cm = 0.394 pouces

Exemple :
Un écran de 17 pouces de diagonale, correspond à 43,18 cm (=17*2.54)

Voici comment votre programme doit se comporter :
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
- fin du programme.
"""


def effectuer_conversion(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Précisez la valeur en {unit1} que vous souhaitez convertir en {unit2}. (ou 'q' pour quiter): ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR: Vous devez rentrer une valeur numérique")
        print("(utilisez le point et non la virgule pour les décimales)")
        return effectuer_conversion(unit1, unit2, facteur)

    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"{valeur_str} {unit1}, correspond à {str(valeur_convertie)} {unit2}")
    return False


def choix_conversion():
    print("Faites votre choix parmi les différentes options de conversion.")
    print("1 - pouces vers cm")
    print("2 - cm vers pouces")
    return input("Votre choix (1 ou 2): ")


while True:
    choice = choix_conversion()
    if choice == "1" or choice == "2":
        break
    print("ERREUR: Vous devez choisir 1 ou 2\n")

while True:
    if choice == "1":
        if effectuer_conversion("pouces", "cm", 2.54):
            break
    if choice == "2":
        if effectuer_conversion("cm", "pouces", 0.394):
            break
