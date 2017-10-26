from .Controlador import *
from .Base import *

def dibujo(fondo, ventana, colores, No_Printees):

    Controlador.rellenar_pantalla(ventana, fondo, colores, No_Printees)
    Base.sprites.draw(ventana)
    pygame.display.flip()