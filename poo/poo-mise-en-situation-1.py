# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom
        self.age = age
        self.genre = genre

    def SePresenter(self):
        print(f"Bonjour, je m'appelle {self.nom}, j'ai {str(self.age)} ans")
        genre_str = "Masculin" if self.genre else "Feminin"
        print(f"Genre : {genre_str}")
        e_optionnel = "" if self.genre else "e"
        est_majeur_str = "majeur" if self.EstMajeur() else "mineur"
        print(f"Je suis {est_majeur_str}{e_optionnel}")
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()