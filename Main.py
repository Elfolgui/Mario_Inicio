from Clases import *

Controlador.iniciar()

colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}

ancho = 1250
alto = 720

fps = 120

fondo = Fondo()

ventana = Controlador.configurar_pantalla(ancho, alto)

reloj = Controlador.iniciar_reloj()

Controlador.Inicializar_Titulo()
Controlador.Inicializar_Subtitulo()

frames_totales = 0

delay = 0

frame = frames_totales

Animacion = True

while True:
    if Acciones(reloj, fps):
        fondo.activo = False

    Controlador.Mover_Titulo(Base.letras_activas_titulo)

    if frame + delay < frames_totales:
        frame = Controlador.Proxima_Letra_Titulo(Base.letras_pasivas_titulo, frames_totales)

    Controlador.Proxima_Letra_Subtitulo(Base.letras_pasivas_subtitulo)
    Controlador.Mover_Subtitulo(Base.letras_activas_subtitulo)

    Dibujo.dibujo(fondo, ventana, colores)

    delay += 5

    if delay == 35:
        delay = 0

    frames_totales += 1