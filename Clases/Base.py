from .Grupo_Sprites import *

class Base(pygame.sprite.Sprite):

    letras_activas_titulo = Sprites()
    letras_activas_subtitulo = Sprites()
    letras_pasivas_titulo = Sprites()
    letras_pasivas_subtitulo = Sprites()
    sprites = Sprites()

    def __init__(self, x, y, ancho, alto, ruta):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(ruta)
        self.image = pygame.transform.scale(self.image, (ancho, alto))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ancho = ancho
        self.alto = alto
