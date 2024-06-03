class Persona:
    def __init__(self, nombre, edad ):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad,  sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

empleado1 = Empleado('Juan', 28, 21231)
print(empleado1.nombre)

