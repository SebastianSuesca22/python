class persona:
    def __init__(self,nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    def mostarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

persona1=persona('Juan','Apellido', 28, '38183183812', 2, 3, 5, m='manzana', p ='Pera')
persona.mostarDetalle(persona1)
