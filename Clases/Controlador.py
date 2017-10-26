from .Base import Base
import pygame
from .Letras import Letra
from .Fin import Final

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
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                return True


    @classmethod
    def Inicializar_Titulo(self):

        S = Letra(80, 200, 80, 100, "letras/titulo/Titulo1.png", False)
        u = Letra(162, 200, 80, 100, "letras/titulo/Titulo2.png", False)
        p = Letra(244, 200, 80, 100, "letras/titulo/Titulo3.png", False)
        e = Letra(328, 200, 80, 100, "letras/titulo/Titulo4.png", False)
        r = Letra(410, 200, 80, 100, "letras/titulo/Titulo5.png", False)

        p = Letra(512, 200, 80, 100, "letras/titulo/Titulo6.png", False)
        o = Letra(594, 200, 80, 100, "letras/titulo/Titulo7.png", False)
        l = Letra(674, 200, 80, 100, "letras/titulo/Titulo8.png", False)
        i = Letra(755, 200, 60, 100, "letras/titulo/Titulo9.png", False)

        b = Letra(840, 200, 80, 100, "letras/titulo/Titulo10.png", False)
        r = Letra(920, 200, 80, 100, "letras/titulo/Titulo11.png", False)
        o = Letra(1000, 200, 80, 100, "letras/titulo/Titulo12.png", False)
        S = Letra(1080, 200, 80, 100, "letras/titulo/Titulo13.png", False)

    @classmethod
    def Inicializar_Subtitulo(self):

        a = Letra(400, 400, 50, 70, "letras/Subtitulo/Letra1.png", True)
        t = Letra(450, 400, 50, 70, "letras/Subtitulo/Letra2.png", True)
        r = Letra(500, 400, 50, 70, "letras/Subtitulo/Letra3.png", True)
        e = Letra(550, 400, 50, 70, "letras/Subtitulo/Letra4.png", True)
        v = Letra(600, 400, 50, 70, "letras/Subtitulo/Letra5.png", True)
        e = Letra(650, 400, 50, 70, "letras/Subtitulo/Letra4.png", True)
        t = Letra(700, 400, 50, 70, "letras/Subtitulo/Letra2.png", True)
        e = Letra(750, 400, 50, 70, "letras/Subtitulo/Letra4.png", True)

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

    @classmethod
    def Inicializacion_Final(cls):

        c1 = Final(0, 0, 1360, 720, "Transicion_Final/Parte1.png")
        c2 = Final(0, 0, 1360, 720, "Transicion_Final/Parte2.png")
        c3 = Final(0, 0, 1360, 720, "Transicion_Final/Parte3.png")
        c4 = Final(0, 0, 1360, 720, "Transicion_Final/Parte4.png")
        c5 = Final(0, 0, 1360, 720, "Transicion_Final/Parte5.png")
        c6 = Final(0, 0, 1360, 720, "Transicion_Final/Parte6.png")
        c7 = Final(0, 0, 1360, 720, "Transicion_Final/Parte7.png")
        c8 = Final(0, 0, 1360, 720, "Transicion_Final/Parte8.png")
        c9 = Final(0, 0, 1360, 720, "Transicion_Final/Parte9.png")
        c10 = Final(0, 0, 1360, 720, "Transicion_Final/Parte10.png")
        c11 = Final(0, 0, 1360, 720, "Transicion_Final/Parte11.png")
        c12 = Final(0, 0, 1360, 720, "Transicion_Final/Parte12.png")
        c13 = Final(0, 0, 1360, 720, "Transicion_Final/Parte13.png")
        c14 = Final(0, 0, 1360, 720, "Transicion_Final/Parte14.png")
        c15 = Final(0, 0, 1360, 720, "Transicion_Final/Parte15.png")
        c16 = Final(0, 0, 1360, 720, "Transicion_Final/Parte16.png")
        c17 = Final(0, 0, 1360, 720, "Transicion_Final/Parte17.png")
        c18 = Final(0, 0, 1360, 720, "Transicion_Final/Parte18.png")
        c19 = Final(0, 0, 1360, 720, "Transicion_Final/Parte19.png")
        c20 = Final(0, 0, 1360, 720, "Transicion_Final/Parte20.png")

        Lista_Negra = [c1, c2, c3, c4, c5,
                       c6, c7, c8, c9, c10,
                       c11, c12, c13, c14, c15,
                       c16, c17, c18, c19, c20]

        return Lista_Negra