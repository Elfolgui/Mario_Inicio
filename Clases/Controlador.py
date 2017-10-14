import pygame
from .Base import Base
from .Titulo import Titulo
from .Subtitulo import Subtitulo
from .Inicializacion import inicializacion

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
        if fondo.activo:
            ventana.blit(fondo.image, fondo.rect)
        if not fondo.activo:
            inicializacion()

    @classmethod
    def buscar_eventos(cls, Grupo):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cls.terminar()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                cls.terminar()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                for sprite in Grupo:
                    Grupo.remove(sprite)
                return True


    @classmethod
    def Inicializar_Titulo(cls):
        S = Titulo(80, 200, 80, 100, "Letras/Titulo/Titulo1.png")
        u = Titulo(162, 200, 80, 100, "Letras/Titulo/Titulo2.png")
        p = Titulo(244, 200, 80, 100, "Letras/Titulo/Titulo3.png")
        e = Titulo(328, 200, 80, 100, "Letras/Titulo/Titulo4.png")
        r = Titulo(410, 200, 80, 100, "Letras/Titulo/Titulo5.png")

        p = Titulo(512, 200, 80, 100, "Letras/Titulo/Titulo6.png")
        o = Titulo(594, 200, 80, 100, "Letras/Titulo/Titulo7.png")
        l = Titulo(662, 200, 80, 100, "Letras/Titulo/Titulo8.png")
        i = Titulo(742, 200, 60, 100, "Letras/Titulo/Titulo9.png")

        b = Titulo(822, 200, 80, 100, "Letras/Titulo/Titulo10.png")
        r = Titulo(902, 200, 80, 100, "Letras/Titulo/Titulo11.png")
        o = Titulo(982, 200, 80, 100, "Letras/Titulo/Titulo12.png")
        S = Titulo(1062, 200, 80, 100, "Letras/Titulo/Titulo13.png")

    @classmethod
    def Inicializar_Subtitulo(cls):

        a = Subtitulo(400, 350, 50, 70, "Letras/Subtitulo/Letra1.png")
        t = Subtitulo(450, 350, 50, 70, "Letras/Subtitulo/Letra2.png")
        r = Subtitulo(500, 350, 50, 70, "Letras/Subtitulo/Letra3.png")
        e = Subtitulo(550, 350, 50, 70, "Letras/Subtitulo/Letra4.png")
        v = Subtitulo(600, 350, 50, 70, "Letras/Subtitulo/Letra5.png")
        e = Subtitulo(650, 350, 50, 70, "Letras/Subtitulo/Letra6.png")
        t = Subtitulo(700, 350, 50, 70, "Letras/Subtitulo/Letra7.png")
        e = Subtitulo(750, 350, 50, 70, "Letras/Subtitulo/Letra8.png")

    @classmethod
    def Proxima_Letra_Titulo(cls, Grupo, frames_totales):
        minimo = 10000000
        L = 0
        if len(Grupo) != 0:
            for Letra in Grupo:
                if Letra.rect.x < minimo:
                    minimo = Letra.rect.x
                    L = Letra
            L.Subiendo = True
            # L.maximo = L.rect.y - 50
            # L.minimo = L.rect.y + 150
            Base.letras_pasivas_titulo.remove(L)
            Base.letras_activas_titulo.add(L)
        return frames_totales

    @classmethod
    def Proxima_Letra_Subtitulo(cls, Grupo):
        minimo = 10000000
        L = 0
        if len(Grupo) != 0:
            for Letra in Grupo:
                if Letra.rect.x < minimo:
                    minimo = Letra.rect.x
                    L = Letra
            L.Subiendo = True
            # L.maximo = L.rect.y - 50
            # L.minimo = L.rect.y + 150
            Base.letras_pasivas_subtitulo.remove(L)
            Base.letras_activas_subtitulo.add(L)

    @classmethod
    def Mover_Titulo(cls, Grupo):
        for letra in Grupo:
            if letra.Subiendo:
                letra.rect.y -= 5
                if letra.rect.y < 175:
                    letra.Subiendo = False
                    letra.Bajando = True
            if letra.Bajando:
                letra.rect.y += 5
                if letra.rect.y >= 225:
                    letra.Subiendo = True
                    letra.Bajando = False

    @classmethod
    def Mover_Subtitulo(cls, Grupo):
        for letra in Grupo:
            letra.maximo = letra.rect.y - 50
            letra.minimo = letra.rect.y + 150
            if letra.Subiendo:
                letra.rect.y -= 5
                if letra.rect.y <= 325:
                    letra.Subiendo = False
                    letra.Bajando = True
            if letra.Bajando:
                letra.rect.y += 5
                if letra.rect.y >= 375:
                    letra.Subiendo = True
                    letra.Bajando = False

    # @classmethod
    # def Mover_Letra(cls, Letra, Animacion):
    #     Original = Letra.rect.y
    #     if Animacion:
    #         if Letra.Subiendo:
    #             Letra.rect.y -= 5
    #             if Letra.rect.y <= 150:
    #                 Letra.Subiendo = False
    #                 Letra.Bajando = True
    #         if Letra.Bajando:
    #             Letra.rect.y += 5
    #             if Letra.rect.y >= 250:
    #                 print("Subo")
    #                 Letra.Subiendo = True
    #                 Letra.Bajando = False
    #         if Letra.rect.y == Original and Letra.Bajando:
    #             print("Entre")
    #             Letra.Subiendo = False
    #             return "Siguiente"
