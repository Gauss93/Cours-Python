class CompteBancaire:
    def __init__(self, solde):
        self.solde = solde

    def deposer(self, montant):
        self.solde = self.solde + montant

    def retirer(self, montant):
        self.solde = self.solde - montant

compte1 = CompteBancaire(1000)

compte1.deposer(200)
print(compte1.solde)
compte1.deposer(600)
print(compte1.solde)
compte1.retirer(150)
print(compte1.solde)
compte1.retirer(350)
print(compte1.solde)