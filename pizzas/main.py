
def afficher(collection, n_premiers=-1):
    n_premier_collection = collection
    if not n_premiers == -1:
        n_premier_collection = collection[0:n_premiers]
    if len(n_premier_collection) == 0:
        print("AUCUNE PIZZA")
        return
    print(f"--- LIST DES PIZZAS ({len(n_premier_collection)}) ---")
    for c in n_premier_collection:
        print(c)
    print()
    print("Première pizza", n_premier_collection[0])
    print("Dernière pizza", n_premier_collection[-1])


def ajouter(collection):
    pizza = input("Pizza à ajouter: ")
    # if not pizza_existe(pizza, collection):
    if pizza.lower() in collection:
        print("ERREUR: cette pizza existe déjà")
    else:
        collection.append(pizza)



def pizza_existe(element, collection):
    for c in collection:
        if c.lower() == element.lower():
            return True
    return False


pizzas = ["4 fromages", "végétarienne", "hawai", "calzon"]
prix = []
ajouter(pizzas)
afficher(pizzas, 3)
