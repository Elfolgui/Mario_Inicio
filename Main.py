from Clases import *
import pygame

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

Devolucion = False

Termine = False

delay = 10

frame = frames_totales

otros_frames = frames_totales

Contador = 0

No_Printees = False

Lista_Negra = Controlador.Inicializacion_Final()

#pygame.mixer.music.load("menu_principal.wav")

#pygame.mixer.music.play(2,0)
#pygame.mixer.music.set_volume(0.25)

while True:

    Controlador.set_fps(reloj, fps)

    if Controlador.buscar_eventos():
        Devolucion = True

    if Devolucion:
        Termine = True
        Base.sprites.add(Lista_Negra[Contador])
        if Contador >= 19:
            Devolucion = False
        Contador += 1
        otros_frames = frames_totales

    if Contador == 19 and otros_frames < frames_totales:
        otros_frames = frames_totales
        for sprite in Base.sprites:
            Base.sprites.remove(sprite)
        No_Printees = True

    if not Termine:
        Controlador.mover()
        if frame + delay < frames_totales:
            if len(Base.letras_pasivas) > 0:
                frame = Controlador.proxima_letra(frames_totales)

    Dibujo.dibujo(fondo, ventana, colores, No_Printees)

    delay += 5

    if delay == 15:
        delay = 5

    frames_totales += 1