
class Pizza:
    def __init__(self, name: str, price: float, ingredients: tuple, isVegetarian: bool = False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.isVegetarian = isVegetarian

    def Show(self):
        description = f" - Végétarienne" if self.isVegetarian else ""
        print(f"Pizza: {self.name} : {self.price}€" + description)
        print(", ".join(self.ingredients))
        print()

class PizzaPersonalized(Pizza):
    STARTING_PRICE = 7
    PRICE_PER_INGREDIENT = 1.2
    LAST_NUMBER = 0

    def __init__(self):
        PizzaPersonalized.LAST_NUMBER += 1
        self.number = PizzaPersonalized.LAST_NUMBER
        super().__init__("Personalisée " + str(self.number), 0, [])
        self.askIngredient()
        self.calculateThePrice()

    def askIngredient(self):
        print()
        print(f"Ingredients pour la pizza personnalisée {self.number}")
        while True:
            ingredient = input("Ajoutez un ingédient (ou ENTRE pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")

    def calculateThePrice(self):
        self.price = PizzaPersonalized.STARTING_PRICE + len(self.ingredients) * PizzaPersonalized.PRICE_PER_INGREDIENT

pizzas = [
    Pizza("Hawai", 9.5, ("tomates", "ananas", "oignons")),
    Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True),
    Pizza("Margarita", 11.50, ("tomates", "huile d'olive", "mozzarella", "basilic")),
    Pizza("Marinara", 8.50, ("tomates", "huile d'olive", "origan", "ail")),
    Pizza("Reine", 10.50, ("oignon", "champignons de Paris", "olives noires", "basilic")),
    Pizza("Végétarienne", 7.80, ("champigons", "tomates", "oignons", "poivrons"), True),
    PizzaPersonalized(),
    PizzaPersonalized()
]

# def tri(e):
#     return e.price

# pizzas.sort(key=tri, reverse=True)

# pizza1 = Pizza("Margarita", 10.50, ("tomates", "huile d'olive", "mozzarella", "basilic"))
# pizza1.Show()

for pizza in pizzas:
    # if "tomates" in pizza.ingredients:
    # if pizza.price <= 10:
    pizza.Show()
