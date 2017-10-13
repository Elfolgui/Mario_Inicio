from .Base import *

class Letra(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)

        self.Subiendo = False
        self.Bajando = False

        Base.letras_titulo.add(self)
        Base.sprites.add(self)