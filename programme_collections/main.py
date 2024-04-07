"""noms = []
while True:
    nom = input("Nom de la personne: ")
    if len(nom) == 0:
        break
    noms.append(nom)

print(*noms)"""

nom_chauffeur = ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
index_min = 0
d_min = distance_chauffeur_km[0]
for i in range(1, len(distance_chauffeur_km)):
    if d_min > distance_chauffeur_km[i]:
        d_min = distance_chauffeur_km[i]
        index_min = i
print(f"L'index de la distance minimale est {index_min}")
print(f"La distance minimale est {d_min} km")
print(f"Nom du chauffeur {nom_chauffeur[index_min]}")

"""noms_et_distances = [
    ("Patrick", 1.5),
    ("Paul", 2.2),
    ("Marc", 0.4),
    ("Jean", 0.9),
    ("Pierre", 7.1),
    ("Marie", 1.1),
    ("Maxime", 0.6)
]

nom_et_distance_min = noms_et_distances[0]
for nom_et_distance in noms_et_distances:
    if nom_et_distance_min[1] > nom_et_distance[1]:
        nom_et_distance_min = nom_et_distance

print(f"Nom du chauffeur {nom_et_distance_min[0]} pour la distance minimale est {nom_et_distance_min[1]} km")"""
