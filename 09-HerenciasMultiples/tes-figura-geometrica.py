from cuadrado import *
from rectangulo import *

#No se puede instanciar una clase abstracta
#figura = figuraGeometrica()
 
cuadrado1 = cuadrado(lado =5,color ='Rojo')
cuadrado1.alto = -10
#MRO -method Resolution Order
# print(cuadrado.mro())
print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

rectangulo1= Rectangulo(ancho=9, alto=8 ,color='verde')
rectangulo1.ancho = 15

print(f'Calculo de area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

print(cuadrado.mro())