from .Letras import *

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
    def Inicializar_Letras(self):
        S = Letra(80, 200, 80, 100, "Letras/Titulo/Titulo1.png")
        u = Letra(160, 200, 80, 100, "Letras/Titulo/Titulo2.png")
        p = Letra(240, 200, 80, 100, "Letras/Titulo/Titulo3.png")
        e = Letra(320, 200, 80, 100, "Letras/Titulo/Titulo4.png")
        r = Letra(400, 200, 80, 100, "Letras/Titulo/Titulo5.png")

        p = Letra(500, 200, 80, 100, "Letras/Titulo/Titulo6.png")
        o = Letra(580, 200, 80, 100, "Letras/Titulo/Titulo7.png")
        l = Letra(660, 200, 80, 100, "Letras/Titulo/Titulo8.png")
        i = Letra(740, 200, 80, 100, "Letras/Titulo/Titulo9.png")

        b = Letra(840, 200, 80, 100, "Letras/Titulo/Titulo10.png")
        r = Letra(920, 200, 80, 100, "Letras/Titulo/Titulo11.png")
        o = Letra(1000, 200, 80, 100, "Letras/Titulo/Titulo12.png")
        S = Letra(1080, 200, 80, 100, "Letras/Titulo/Titulo13.png")

    @classmethod
    def Proxima_Letra(cls, Grupo):
        minimo = 10000000
        L = 0
        if len(Grupo) != 0:
            for Letra in Grupo:
                if Letra.rect.x < minimo:
                    minimo = Letra.rect.x
                    L = Letra
            L.Subiendo = True
            Base.letras_titulo.remove(L)
            return L
        return True

    @classmethod
    def Mover_Letra(cls, Letra, Animacion):
        if Animacion:
            Original = Letra.rect.y
            if Letra.Subiendo:
                Letra.rect.y -= 10
                if Letra.rect.y <= 150:
                    Letra.Subiendo = False
                    Letra.Bajando = True
            if Letra.Bajando:
                Letra.rect.y += 10
                if Letra.rect.y >= 250:
                    Letra.Subiendo = True
                    Letra.Bajando = False
            if Letra.rect.y >= Original and Letra.Subiendo:
                print("Entre")
                Letra.Subiendo = False
                return "Siguiente"


    # @classmethod La Gorda Tiene Sueño
    # def Mover_Letras(cls):