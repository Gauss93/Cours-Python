class CompteBancaire:
    def __init__(self, solde):
        self.solde = solde

compte1 = CompteBancaire(100)
compte2 = CompteBancaire(1000)

compte2.solde -= 500

print(compte1.solde)
print(compte2.solde)