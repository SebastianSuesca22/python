class persona:
    def __init__(self,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1=persona('Juan','Apellido', 28)
print(f'Obejto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}' )

persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Juarez'
persona1.edad = 25
print(f'Obejto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}' )

persona2=persona('Sebastian','Suesca',22)
print(f'Obejto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}' )


