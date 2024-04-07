class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom
        self.age = age
        if len(self.nom) == 0:
            self.DemanderNom()

    def SePresenter(self):
        info_personne = f"Bonjour, Je m'appelle {self.nom}"
        if self.age:
            info_personne += f", j'ai {self.age} ans"
        print(info_personne)

        if self.age:
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18

    def DemanderNom(self):
        self.nom = input("Quelle est le nom de la personne: ")

class Etudiant(Personne):
    def __init__(self, nom: str, age: int, etudes: str):
        super().__init__(nom, age)
        self.etudes = etudes

    def SePresenter(self):
        super().SePresenter()
        print(f"Je suis etudiant en {self.etudes}")

personne1 = Personne("Jena", 30)
personne2 = Personne("Paul", 15)

personne1.SePresenter()
personne2.SePresenter()

etudiant = Etudiant("Marc", 22, "Ecole d'ingénieur informatique")
etudiant.SePresenter()
