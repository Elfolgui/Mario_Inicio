from .Base import *

class Fondo(Base):

    def __init__(self):

        Base.__init__(self, 0, 0, 1280, 720, "imagenes/fondo.jpg")