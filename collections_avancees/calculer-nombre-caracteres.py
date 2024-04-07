noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

# Completion de liste
longeur_nom = [len(nom) for nom in noms]
print("Nombre total des caractère:", sum(longeur_nom))

noms_join = "".join(noms)
print("Nombre total des caractère:", len(noms_join))