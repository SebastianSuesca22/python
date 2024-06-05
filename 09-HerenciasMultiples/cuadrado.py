from figuraGeometrica import *
from color import *


class cuadrado (figuraGeometrica, Color):
    def __init__(self, lado, color):
        #super().__init__(alto)
        figuraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self) -> str:
        return f'{figuraGeometrica.__str__(self)} {Color.__str__(self)}'