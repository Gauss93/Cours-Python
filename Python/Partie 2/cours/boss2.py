import random

class Plante:
    def __init__(self):
        self.mure = 3
        self.pousse = 1
        self.prix_recolte = 5
        self.est_recoltee = False

    def calculer_recolte(self):
        pass

class Mais(Plante):
    def __init__(self):
        super().__init__()
        self.mure = 2

    def calculer_recolte(self):
       chance = random.choice([True, False])
       if chance:
            self.prix_recolte = 10

class Pommier(Plante):
    def __init__(self):
        super().__init__()

    def calculer_recolte(self):
        if self.est_recoltee:
            self.est_recoltee = False
            self.pousse = 0

class Truffe(Plante):
    def __init__(self):
        super().__init__()
        self.mure = 5
        self.prix_recolte = 11


class Temps:
    def __init__(self):
        self.jour = 1
        self.piece = 0
        self.plante_en_culture = []

    

