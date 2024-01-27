def choix_conversion():
    print("Faites votre choix parmi les différentes options de conversion.")
    print("A. pouces vers cm")
    print("B. cm vers pouces")
    choix = input("Indiquez votre choix entre A et B: ")
    while not choix == "A" and not choix == "B":
        print("Veuillez faire un choix entre A et B. Réessayez.")
        print()
        choix = input("Indiquez votre choix entre A et B: ")
    return choix


CONVERSTION_UNITE = 2.54


def conversion_unite(choix, val_str, u_input, u_output):
    unite = CONVERSTION_UNITE
    if choix == "B":
        unite = round(1/CONVERSTION_UNITE, 3)

    valeur_float = 0
    valeur = 0
    while valeur_float == 0:
        try:
            valeur_float = float(val_str)
            valeur = round(valeur_float * unite, 2)
        except:
            print("Erreur: Veillez entrer une valeur valide")
            print()
            val_str = input("Entrez une valeur valide: ")
            valeur_float = 0
    if valeur > 0:
        print(f"{val_str} {u_input}, correspond à {str(valeur)} {u_output}")


type_conversion = choix_conversion()
unite_input = "pouces"
unite_output = "cm"
if type_conversion == "B":
    unite_input = "cm"
    unite_output = "pouces"

valeur_str = input(f"Précisez la valeur en {unite_input} que vous souhaitez convertir en {unite_output}.: ")
conversion_unite(type_conversion, valeur_str, unite_input, unite_output)

