from Clases import *

Controlador.iniciar()

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

ancho = 1250
alto = 720

fps = 120

fondo = Fondo()

ventana = Controlador.configurar_pantalla(ancho, alto)

reloj = Controlador.iniciar_reloj()

Controlador.Inicializar_Letras()

aux = 13

Proxima = Controlador.Proxima_Letra(Base.letras_titulo, aux)

while True:
    Acciones(reloj, fps)
    if Controlador.Mover_Letra(Proxima) == "Siguiente":
        Proxima = Controlador.Proxima_Letra(Base.letras_titulo, aux)
    Dibujo.dibujo(fondo, ventana, colores)
