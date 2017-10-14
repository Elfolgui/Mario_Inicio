from .Controlador import *

class Piso(Base):

    def __init__(self, x, y):
        Base.__init__(self, x, y, 72, 71, "imagenes/piso_bloque.png")

        Base.sprites.add(self)
        Base.piso.add(self)