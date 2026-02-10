class Mamie:
    def __init__(self, nom):
        self.nom = nom
        self.niveau = 1
        self.exp = 0
        self.capacite = 1
        self.retraite = False

    def produire(self):
        if self.retraite:
            return 0, f"{self.nom} est à la retraite."

        cookies_produits = self.capacite
        self.exp += 1

        message = f"{self.nom} produit {cookies_produits} cookies."

        self._evoluer()

        return cookies_produits, message

    def _evoluer(self):
        if self.exp >= 3:
            self.exp = 0
            self.niveau += 1

            if self.niveau < 4:
                self.capacite = self.niveau
            elif self.niveau == 4:
                self.capacite = 6
            else:
                self.retraite = True
                self.capacite = 0
class Jeu:
    def __init__(self):
        self.cookies = 0
        self.objectif = 200
        self.prix_mamie = 3

        self.noms_mamies = [
            "Gertrude", "Jeanette", "Yvonne",
            "Otilia", "Marie-Antoinette", "Elisabeth"
        ]

        self.mamies = []

    def cuisiner(self):
        self.cookies += 1

    def acheter_mamie(self):
        if self.cookies < self.prix_mamie:
            return "Pas assez de cookies."

        if not self.noms_mamies:
            return "Plus de mamies disponibles."

        nom = self.noms_mamies.pop(0)
        self.mamies.append(Mamie(nom))
        self.cookies -= self.prix_mamie
        self.prix_mamie += 2

        return f"Mamie {nom} recrutée."

    def produire(self):
        messages = []

        for mamie in self.mamies:
            produits, message = mamie.produire()
            self.cookies += produits
            messages.append(message)

        return messages

    def objectif_atteint(self):
        return self.cookies >= self.objectif
def lancer_jeu():
    jeu = Jeu()

    while True:
        print(f"\nCookies : {jeu.cookies}")
        print(f"Objectif : {jeu.objectif}")
        print("1 : Cuisiner un cookie")
        print(f"2 : Acheter une mamie ({jeu.prix_mamie} cookies)")

        try:
            action = int(input("Action : "))

            if action == 1:
                jeu.cuisiner()
            elif action == 2:
                print(jeu.acheter_mamie())
            else:
                print("Action invalide.")

            for msg in jeu.produire():
                print(msg)

            if jeu.objectif_atteint():
                print("\nBRAVO ! Objectif atteint.")
                break

        except ValueError:
            print("Entrée invalide.")

lancer_jeu()