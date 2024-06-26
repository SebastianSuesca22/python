class Persona:
    def __init__(self,nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    @property 
    def nombre(self):
        return self._nombre
    @property 
    def apellido( self):
        return self._apellido
    @property 
    def edad(self):
        return self._edad
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido
    @edad.setter
    def edad (self, edad):
        self._edad = edad    

    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
    def __del__ (self):
        print(f'Persona: {self._nombre} {self._apellido}')

if __name__ == '__main__':
    persona1=Persona('Juan','Perez', 28)
    persona1.nombre = 'Juan Carlos'
    persona1.apellido = 'Lara'
    persona1.edad = 30
    persona1.mostrarDetalle()
    
    print(__name__)
