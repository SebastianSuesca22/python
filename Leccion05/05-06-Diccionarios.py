diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)
#largo
print(len(diccionario))
#acceder a un elemento (key)
print(diccionario['IDE'])
#otra forma de recuperar un elemento
print(diccionario.get('OOP'))
#modelificar elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

#recorrer los elementos
for termino, valor in diccionario.items():
    print(termino,valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#comprobar existencia de algun valor
print('IDE' in diccionario)

#agregar un elemento 

diccionario['PK'] = 'Primary key'
print(diccionario)

#remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#limpiar los elementos sin el diccionario
diccionario.clear()
print(diccionario)