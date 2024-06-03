class persona:
    def __init__(self,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1=persona('Juan','Apellido', 28)
persona.mostarDetalle(persona1)
persona1.telefono = '5542423'


persona2=persona('Sebastian','Suesca',22)
persona2.mostarDetalle()


