from .Controlador import *
from .Base import *
from .Colocacion import inicializacion

def dibujo(fondo, ventana, colores):

    Controlador.rellenar_pantalla(ventana, fondo, colores)
    Base.sprites.draw(ventana)
    pygame.display.flip()