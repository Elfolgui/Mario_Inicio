from clases import *

Controlador.iniciar()

colores = {"Blanco": (255, 255, 255), "Negro": (0, 0, 0)}

ancho = 1280
alto = 720

fps = 120

fondo = Fondo()

ventana = Controlador.configurar_pantalla(ancho, alto)

reloj = Controlador.iniciar_reloj()

Controlador.Inicializar_Titulo()
Controlador.Inicializar_Subtitulo()

frames_totales = 0

delay = 10

frame = frames_totales

while True:

    Controlador.set_fps(reloj, fps)
    Controlador.buscar_eventos()

    Controlador.mover()

    if frame + delay < frames_totales:
        if len(Base.letras_pasivas) > 0:
            frame = Controlador.proxima_letra(frames_totales)

    Dibujo.dibujo(fondo, ventana, colores)

    delay += 5

    if delay == 40:
        delay = 10

    frames_totales += 1