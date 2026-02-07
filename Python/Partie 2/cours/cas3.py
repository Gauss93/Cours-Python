class perso:
    def __init__(self, nom, pdv):
        self.nom = nom
        self.pdv = pdv

    def takedamage(self, damage):
        self.pdv = self.pdv - damage

perso1 = perso("joueur", 100) 
perso2 = perso1
perso2.takedamage(30)
print(perso1.pdv)
print(perso2.pdv)

perso3 = perso("joueur3", 100)
perso4 = perso("joueur4", 100)
perso4.takedamage(40)
print(perso3.pdv)
print(perso4.pdv)