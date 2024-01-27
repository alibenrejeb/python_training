import random


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"quel est le nombre magique (entre {nb_min} et {nb_max})? ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Le nombre doit être entre {nb_min} et {nb_max}. Réessayez.")
                nombre_int = 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4

"""nombre = 0
vies = NB_VIES
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre < NOMBRE_MAGIQUE:
        print("Le nombre magique est plus grand")
        vies -= 1
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies -= 1
    else:
        print("Bravo, vous avez gagné")

if vies == 0:
    print(f"Vous avez perdu! le nombre magique était: {NOMBRE_MAGIQUE}")"""

nombre = 0
gagner = False
for i in range(0, NB_VIES):
    vies = NB_VIES - i
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre < NOMBRE_MAGIQUE:
        print("Le nombre magique est plus grand")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
    else:
        print("Bravo, vous avez gagné")
        gagner = True
        break

if not gagner:
    print(f"Vous avez perdu! le nombre magique était: {NOMBRE_MAGIQUE}")
