class calcularCubo:
    def __init__(self, ancho, profundo,alto) -> None:
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto
    def volumen(self):
        return self.ancho * self.profundo * self.alto

ancho = float(input('Ingrese el ancho del cubo: '))
profundo = float(input('Ingrese el profundo del cubo: '))
alto = float(input('Ingrese el alto del cubo: '))

calcularCubo1 = calcularCubo(ancho, profundo, alto)

print(f'El volumen del cubo es: {calcularCubo1.volumen():.2f}, m3')