class areaRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

altura = float(input('Ingrese la base del triangulo: '))
base = float (input('Ingrese la base del triangulo: '))
areaRectangulo1=areaRectangulo(altura, base)
print(f'El area del triangulo es: {areaRectangulo1.area()}')

