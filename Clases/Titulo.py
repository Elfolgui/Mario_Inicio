from .Letras import *

class Titulo(Letra):

    def __init__(self, x, y, ancho, alto, ruta):
        Letra.__init__(self, x, y, ancho, alto, ruta)

        Base.letras_pasivas_titulo.add(self)