from .Letras import *

class Subtitulo(Letra):

    def __init__(self, x, y, ancho, alto, ruta):
        Letra.__init__(self, x, y, ancho, alto, ruta)

        Base.letras_pasivas_subtitulo.add(self)