cookies = 0
objectif = 10000
prix_mamie = 3
liste_mamie = ["Gertrude", "Jeanette", "Yvonne", "Otilia", "Marie-antoinette", "Elisabeth"]
mamie_en_service = []

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

                

while True: 

    print(f'Nombres de cookies : {cookies}')
    print(f'Objectif de cookies {objectif}')
    print('1 : Cuisiner un cookie')
    print(f'2 : Acheter une mamie (coute {prix_mamie} cookies)') 

    try:

        action = int(input('Action : '))

        if action < 1 or action > 2:
              print('Veuillez choisir une action valide !')

        if action == 1:
            cookies += 1
        elif action == 2 and cookies >= prix_mamie:
            if len(liste_mamie) > 0:
                nom = liste_mamie.pop(0)
                new_mamie = Mamie(nom)
                mamie_en_service.append(new_mamie)
                cookies -= prix_mamie
                prix_mamie += 2
            else:
                  print('Plus de mamie disponible !')
        else:
              print("Vous n'avez pas asser de cookies !")
        
        for m in mamie_en_service:
              m.produire_cookies()
              cookies += m.capacite 
        
        if cookies >= objectif:
              print(f"BRAVO ! Objectif de {objectif} atteint !")
              break

    except ValueError:
                print("Ce n'est pas un chiffre !")

