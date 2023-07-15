class Perso:
    def __init__(self, largeurEcran, hauteurEcran,  nom='kirby',urlBase='img/sprite.png' , transparence=(0,0,0), positionInit=(0,0)):

        self.nom = nom
        self.urlBase = urlBase
        self.transparence = transparence
        self.positionInit = positionInit


    def creerPerso(self):
        persoInstance = self.pygame.image.load(self.urlBase).convert
        return persoInstance
    def positionDepart(self,perso, x, y):
        self.xpos = x
        self.ypos = y
    def mouvements(self):
        self.xpos += x_step
        self.ypos += y_step

    def limiteMouvements(self):
        pass

    def transparence(self):
        self.setcolorkey((self.transparence()))


def creerPerso(largeurEcran, hauteurEcran, param):
    return None