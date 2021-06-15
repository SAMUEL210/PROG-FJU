class Tribu:
    def __init__(self, nom):
        self._nom = nom
        self._points = 0

    def getNom(self):
        return self._nom

    def setNom(self, nouvNom):
        self._nom = nouvNom

    def getPoints(sefl):
        return self._points

    def setPoints(self, nouvPoints):
        self._points = nouvPoints

    def ajouterPoint(self, points):
        self._points += points

    def enleverPoints(self, points):
        self._points -= points
