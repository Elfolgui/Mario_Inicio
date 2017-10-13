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

Proxima = Controlador.Proxima_Letra(Base.letras_titulo)

Animacion = True

while True:
    Acciones(reloj, fps)
    if Controlador.Mover_Letra(Proxima, Animacion) == "Siguiente":
        Proxima = Controlador.Proxima_Letra(Base.letras_titulo)
        if Proxima is True:
            Animacion = False


    Dibujo.dibujo(fondo, ventana, colores)
