class Chanson:
    def __init__(self, titre, artiste, durée):
        self.titre = titre 
        self.artiste = artiste 
        self.durée = durée 

class LectureMusique:
    def __init__(self, chanson, volume):
        self.chanson = chanson
        self.volume = volume

    def jouer(self):
        return f"Lecture de {self.chanson.titre} par {self.chanson.artiste} au volume {self.volume}"

chanson1 = Chanson("Hors-ligne", "Friz corleone", 4.55)
chanson2 = Chanson("Blue Bird", "Opening", 2.32)
chanson3 = Chanson("Don't Stop", "Bigslayy", 10)

playlist = [chanson1, chanson2, chanson3]

for music in playlist:
    reglage = LectureMusique(music, 50)
    print(reglage.jouer())
