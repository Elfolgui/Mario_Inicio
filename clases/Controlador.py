from clases.Base import Base
import pygame
from clases.Letra import Letra

class Controlador(object):

    @classmethod
    def iniciar(cls):
        pygame.init()

    @classmethod
    def terminar(cls):
        pygame.quit()
        quit()

    @classmethod
    def configurar_pantalla(cls, ancho, alto):
        display = pygame.display.set_mode((ancho, alto)) #, pygame.FULLSCREEN
        pygame.display.set_caption("Super Poli Bros")
        return display

    @classmethod
    def iniciar_reloj(cls):
        return pygame.time.Clock()

    @classmethod
    def set_fps(cls, reloj, frames):
        reloj.tick(frames)

    @classmethod
    def rellenar_pantalla(cls, ventana, fondo, colores):
        ventana.fill(colores["Negro"])
        ventana.blit(fondo.image, fondo.rect)

    @classmethod
    def buscar_eventos(cls):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cls.terminar()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                cls.terminar()


    @classmethod
    def Inicializar_Titulo(self):

        S = Letra(80, 200, 80, 100, "imagenes/letras/Titulo/Titulo1.png", False)
        u = Letra(162, 200, 80, 100, "imagenes/letras/Titulo/Titulo2.png", False)
        p = Letra(244, 200, 80, 100, "imagenes/letras/Titulo/Titulo3.png", False)
        e = Letra(328, 200, 80, 100, "imagenes/letras/Titulo/Titulo4.png", False)
        r = Letra(410, 200, 80, 100, "imagenes/letras/Titulo/Titulo5.png", False)

        p = Letra(512, 200, 80, 100, "imagenes/letras/Titulo/Titulo6.png", False)
        o = Letra(594, 200, 80, 100, "imagenes/letras/Titulo/Titulo7.png", False)
        l = Letra(674, 200, 80, 100, "imagenes/letras/Titulo/Titulo8.png", False)
        i = Letra(755, 200, 60, 100, "imagenes/letras/Titulo/Titulo9.png", False)

        b = Letra(840, 200, 80, 100, "imagenes/letras/Titulo/Titulo10.png", False)
        r = Letra(920, 200, 80, 100, "imagenes/letras/Titulo/Titulo11.png", False)
        o = Letra(1000, 200, 80, 100, "imagenes/letras/Titulo/Titulo12.png", False)
        S = Letra(1080, 200, 80, 100, "imagenes/letras/Titulo/Titulo13.png", False)

    @classmethod
    def Inicializar_Subtitulo(self):

        a = Letra(400, 400, 50, 70, "imagenes/letras/Subtitulo/Letra1.png", True)
        t = Letra(450, 400, 50, 70, "imagenes/letras/Subtitulo/Letra2.png", True)
        r = Letra(500, 400, 50, 70, "imagenes/letras/Subtitulo/Letra3.png", True)
        e = Letra(550, 400, 50, 70, "imagenes/letras/Subtitulo/Letra4.png", True)
        v = Letra(600, 400, 50, 70, "imagenes/letras/Subtitulo/Letra5.png", True)
        e = Letra(650, 400, 50, 70, "imagenes/letras/Subtitulo/Letra4.png", True)
        t = Letra(700, 400, 50, 70, "imagenes/letras/Subtitulo/Letra2.png", True)
        e = Letra(750, 400, 50, 70, "imagenes/letras/Subtitulo/Letra4.png", True)

    @classmethod
    def proxima_letra(cls, frames_totales):
        minimo = 2000
        objeto = None

        for letra in Base.letras_pasivas:
            if letra.rect.x < minimo:
                minimo = letra.rect.x
                objeto = letra

        objeto.subiendo = True
        Base.letras_pasivas.remove(objeto)
        Base.letras_activas.add(objeto)
        return frames_totales

    @classmethod
    def mover(cls):

        for letra in Base.letras_activas:

            if letra.subiendo:
                letra.rect.y -= letra.velocidad
                if letra.rect.y < letra.maximo:
                    letra.subiendo = False
                    letra.bajando = True

            if letra.bajando:
                letra.rect.y += letra.velocidad
                if letra.rect.y >= letra.minimo:
                    letra.subiendo = True
                    letra.bajando = False