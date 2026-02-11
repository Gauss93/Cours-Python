class CompteBancaire:
    def __init__(self, solde):
        self._solde = solde

    def deposer(self, montant):
        self.solde = self.solde + montant

    def retirer(self, montant):
        if montant <= self._solde:
            self._solde -= montant

compte1 = CompteBancaire(1000)
compte1.retirer(900)
print(compte1._solde)
compte1.retirer(200)
print(compte1._solde)