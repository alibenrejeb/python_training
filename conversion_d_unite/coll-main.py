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

# unité de départ, unité d'arrivée, facteur de conversion
CONVERSIONS = (
    ("pouces", "cm", 2.54),
    ("m", "cm", 100),
    ("km", "miles", 0.621371),
    ("yard", "m", 0.9144),
)

"""
1 - pouces vers cm      1   0   F
2 - cm vers pouces      2   0   T
3 - m vers cm           3   1   F
4 - cm vers m           4   1   T
5 - km vers miles       5   2   F
6 - miles vers km       6   2   T
"""


def effectuer_conversion(unit1: str, unit2: str, facteur: float, reverse: bool = False):
    if reverse:
        unit1, unit2 = unit2, unit1
        facteur = 1/facteur

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


def demander_valeur_numerique(v_min: int, v_max: int):
    choice_str = input(f"Donnez une valeur entre {v_min} et {v_max}: ")
    try:
        choice_int = int(choice_str)
    except:
        print("ERREUR: Vous devez rentrer une valeur numérique")
        return demander_valeur_numerique(v_min, v_max)
    if not (v_min <= choice_int <= v_max):
        print(f"ERREUR: Vous devez choisir une valeur entre {v_min} et {v_max}\n")
        return demander_valeur_numerique(v_min, v_max)
    return choice_int


def choix_conversion():
    print("Faites votre choix parmi les différentes options de conversion.")
    i = 1
    for c in CONVERSIONS:
        unit1 = c[0]
        unit2 = c[1]
        print(f"{i} - {unit1} vers {unit2}")
        i += 1
        print(f"{i} - {unit2} vers {unit1}")
        i += 1

    return demander_valeur_numerique(1, i - 1)


choice = choix_conversion()

while True:
    # Si le choix utilisateur est 1 alors l'index 0 (premier idem de CONVERSION)
    # Divisé par 2, car on génére des options intermédiaires de conversions inverse
    #   choix = 2 -> index 0 mais reverse = True (conversion inverse)
    index = (choice - 1) // 2
    # 1 % 2 = 0 * 2 + 1
    # 2 % 2 = 1 * 2 + 0
    # 3 % 2 = 1 * 2 + 1
    # 4 % 2 = 2 * 2 + 0
    # True si la valeur est pair
    reverse = choice % 2 == 0
    unit1, unit2, facteur = CONVERSIONS[index]
    if effectuer_conversion(unit1, unit2, facteur, reverse):
        break
