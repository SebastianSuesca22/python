from figuraGeometrica import *
from color import *


class Rectangulo(figuraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        figuraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self) -> str:
        return f'{figuraGeometrica.__str__(self)} {Color.__str__(self)}'
