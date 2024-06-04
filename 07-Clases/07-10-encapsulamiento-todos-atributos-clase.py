class persona:
    def __init__(self,nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    @property 
    def nombre(self):
        print('Llamando metodo get nombre')
        return self._nombre
    @property 
    def apellido( self):
        return self._apellido
    @property 
    def edad(self):
        return self._edad
    
    @nombre.setter
    def nombre(self,nombre):
        print('Llamando metodo set nombre')
        self._nombre = nombre
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido
    @edad.setter
    def edad (self, edad):
        self._edad = edad    

    def mostarDetalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1=persona('Juan','Apellido', 28)
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Salinas'
persona1.edad = 30

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

# persona1._nombre = 'cambio'
# print(persona1._nombre)


#VARIABLES DE SOLO LECTURA