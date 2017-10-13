from .Base import *

class Letra(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)

        self.maximo = 0
        self.minimo = 0

        self.Subiendo = False
        self.Bajando = False

        Base.sprites.add(self)
