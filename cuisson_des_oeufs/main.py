import time
import beepy

ATTENDRE_SEC = 10

NOS_CUISSONS = (
    ("Oeufs à la coque", 3*60),
    ("Oeufs mollets", 6*60),
    ("Oeufs durs", 9*60),
    ("Test 1", 10),
)


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


def attendre_seconde(sec):
    for i in range(sec):
        time.sleep(1)
        print(".", end="", flush=True)


def temps_sec_en_str(t):
    minute = t // 60
    seconde = t - minute * 60
    min_unit = "minute"
    sec_unit = "seconde"
    if minute > 1:
        min_unit += "s"
    if seconde > 1:
        sec_unit += "s"
    reponse = ""
    if minute > 0:
        reponse += f"{minute} {min_unit}"
    if seconde > 0:
        if len(reponse) > 0:
            reponse += " "
        reponse += f"{seconde} {sec_unit}"
    return reponse


def minuteur(d):
    while d > 0:
        minute = d // 60
        seconde = d - minute * 60
        print(f"Temps restant : {minute:02d}:{seconde:02d} ", end="", flush=True)
        attendre_seconde(ATTENDRE_SEC)
        print()
        d -= ATTENDRE_SEC
    print("Cuisson terminée")
    beepy.beep(sound="ping")


print("Veuillez choissier votre cuisson:")
index = 1
for cuisson in NOS_CUISSONS:
    print(f"{index}- {cuisson[0]}: {temps_sec_en_str(cuisson[1])}")
    index += 1

choice = choix_menu(1, index - 1)
duree = NOS_CUISSONS[choice-1][1]
minuteur(duree)
