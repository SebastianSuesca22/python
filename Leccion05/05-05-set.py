planetas = {"marte", "Jupiter", "Venus"} #No guarda orden 
print(planetas)

#largo de los elementos
print(len(planetas))

#revisar si un elemento esta presente
print('marte' in planetas)

planetas.add('Tierra')
print(planetas)

planetas.add('Tierra')
print(planetas)

#eliminar elementos
planetas.remove('Tierra')
print(planetas)

#eliminar elemento sin arrojar error
planetas.discard('jupiters')
print(planetas)