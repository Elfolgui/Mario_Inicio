from .Controlador import *
from .Base import *

def Acciones(reloj, fps):

    Controlador.set_fps(reloj, fps)
    if Controlador.buscar_eventos(Base.sprites):
        return True
