class persona:
    def __init__(self,nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    @property 
    def nombre(self):
        print('Llamando metodo get nombre')
        return self._nombre
    
    # @nombre.setter
    # def nombre(self,nombre):
    #     print('Llamando metodo set nombre')
    #     self._nombre = nombre

    def mostarDetalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1=persona('Juan','Apellido', 28)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)
# persona1._nombre = 'cambio'
# print(persona1._nombre)


#VARIABLES DE SOLO LECTURA