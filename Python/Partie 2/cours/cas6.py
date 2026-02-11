class Notification:
    def __init__(self, heure):
        self.heure = heure
    
    def envoyer(self):
        return f"vous avez reçu une notification à {self.heure} heure"

class NotificationEmail(Notification):
    def __init__(self, heure, expediteur):
        super().__init__(heure)
        self.expediteur = expediteur
    
    def envoyer(self):
        return f"Vous avez reçu un e-mail de la part de {self.expediteur} à {self.heure} heure"

class NotificationBanque(Notification):
    def __init__(self, heure, montant):
        super().__init__(heure)
        self.montant = montant

    def envoyer(self):
        return f"Vous avez effectué un paiement de {self.montant} euros à {self.heure} heure"

liste_notif = [Notification(5), NotificationEmail(5, "La Poste"), NotificationBanque(5, 600)]

for notif in liste_notif:
    print(notif.envoyer())