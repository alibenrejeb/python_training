# LES COLLECTION: LISTES / TUPLES
# Append / Extend / += / Insert

noms = ["Jean", "Sophie", "Martin"]
noms_supplementaires = ["Christophe", "Zoe"]

# noms.append("Toto")
# noms.extend(noms_supplementaires)
noms += noms_supplementaires
# noms.insert(1, "Toto")

# noms = noms_supplementaires + noms
# print(noms)

# Sort /Sorted
# noms.sort(key=lambda elt: len(elt), reverse=True)
nom_tries = sorted(noms, key=lambda elt: len(elt), reverse=True)
# print(nom_tries)

# Operations sur les elements : min, max, in, sum
ages = [21, 20, 30, 25, 22]
"""print(min(ages))
print("Jean" in noms)
print(sum(ages))"""

# Swapper deux éléments (échanger)
noms[0], noms[4] = noms[4], noms[0]
# print(noms)

# join et split
noms_join = ",".join(noms)
"""print(noms_join)
print(noms_join.split(","))"""

# index, find et count
"""noms = ['Zoe', 'Sophie', 'Martin', 'Christophe', 'Alex']
element_cherche = "Martin"
nb_occurences = noms.count(element_cherche)
print("nombre d'occurences: ", nb_occurences)
index_occurence = 0
if nb_occurences > 0:
    for i in range(nb_occurences):
        index_occurence = noms.index(element_cherche, index_occurence)
        # print(element_cherche, "trouvé à", index_occurence)
        index_occurence += 1
else:
    print("L'élément n'est pas dans la collection")"""

# Les comrehensions de listes
"""longeur_noms = []
for nom in noms:
    longeur_noms.append(len(nom))"""

# longeur_noms = [len(nom) for nom in noms if len(nom) < 10]
# longeur_noms = [len(nom) if len(nom) < 10 else 0 for nom in noms ]
# noms_avec_e = [nom for nom in noms if "e" in nom]

# a = [i for i in range(5) if (i//2) * 2 == i] # i%2 == 0
b = [True if (i//2) * 2 == i else False for i in range(5)]
# print(b)

# Any and All
noms = ['Zoe', 'Sophie', 'Martin', 'Christophe', 'Alex']
"""a = [True, False, False, True]
print(any(a))
print(all(a))"""

# print(any([True if "z" in nom.lower() else False for nom in noms]))

# any / isdigit
"""nom = input("Quel est ton nom ? ")
if nom == "":
    print("Le nom est vide")
elif any([c.isdigit() for c in nom]):
    print("Le nom ne doit contenir que des lettres")
else:
    print(f"Bonjour {nom}")"""

# Collections: Zip
"""pizza_noms = ("Pizza 1", "Pizza 2", "Pizza 3")
pizza_prix = (11, 9.5, 10.5)

pizza = list(zip(pizza_noms, pizza_prix))
for (nom, prix) in zip(pizza_noms, pizza_prix):
    print(f"{nom} - {prix}€")

pn, pp = zip(*pizza)
print("ok")"""

# Collections: Le Set
