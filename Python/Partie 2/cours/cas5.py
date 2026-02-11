class Mamie:
    def __init__(self, nom, niveau=1, exp=0):
        self.nom = nom
        self.niveau = niveau
        self.exp = exp
        self.capacite = self.niveau
        self.cookies = 0
        self.est_en_retraite = False


    def produire_cookies(self):
          if self.est_en_retraite:
                self.capacite = 0
                print(f"{self.nom} est à la retraite et ne cuisine plus !")
                return
          
          self.cookies += self.capacite
          self.exp += 1
          print(f'Mamie {self.nom} produit {self.capacite} cookies.')

          self.evoluer()
          self.super_mamie()
          self.retraite()

    def evoluer(self):
          if self.exp >= 3:
                self.niveau += 1
                self.exp = 0

                if self.niveau < 4:
                      self.capacite = self.niveau
                print(f'Mamie {self.nom} passe au niveau {self.niveau}.')

    def super_mamie(self):
          if self.niveau == 4:
                self.capacite = 6
                print(f'Mamie {self.nom} devient une super Mamie !')

    def retraite(self):
          if self.niveau >= 5:
                self.est_en_retraite = True 
                print(f'Mamie {self.nom} prend sa retraite.')
                
    def __str__(self):
          return f'Mamie {self.nom} (niveau {self.niveau})'
    
    def __repr__(self):
          return f'Mamie(nom={self.nom}, niveau={self.niveau})'
    
    def __eq__(self, other):
          return self.niveau == other.niveau


a = Mamie("Gertrude", 2)
b = Mamie("Antoinette", 2)

mamies = [a, b]
print(a , b)
print(mamies)
print(a == b)