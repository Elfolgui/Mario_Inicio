from .Base import *

class Fondo(Base):

    def __init__(self):

        Base.__init__(self, 0, 0, 1250, 720, "Fondos/Primera.jpg")

        self.activo = True

    def Cambiar_Forma(self, Grupo_movil, Grupo_):
        self.ancho -= 10
        self.alto -= 2
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))