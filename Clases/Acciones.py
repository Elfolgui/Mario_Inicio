from .Controlador import *
from .Base import *

def Acciones(reloj, fps):

    Controlador.set_fps(reloj, fps)
    Controlador.buscar_eventos()
