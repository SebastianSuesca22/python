#Definir una lista de tipo str
nombre = ['Juan','Karla','Ricardo','Maria']

#Imprimir la lista de nombres
print(nombre)

#accerder a los elementros de una lista
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])

#Acceder a los elementos de manera inversa
print(nombre[-1])
print(nombre[-2])
print(nombre[-3])
print(nombre[-4])

print(nombre[0:2])
#ir del inicio de la lista al indice (sin incluirlo)

print(nombre[ : 4])

#Desde el indice indicado hasta el final
print(nombre[1: ])

#cambiar un valor 
nombre[3] = 'Ivone'

print(nombre)

#Iterar una lista
for nombres in nombre:
    print(nombres)
else:
    print('No existen mas nombres en la lista')

#preguntar el largo de una lista
print(len(nombre))

#agregar un  elemento
nombre.append('Lorenzo')
print(nombre)

#insertar un elemento en un indice en especifico 
nombre.insert(1,'Octavio')
print(nombre)
#eliminar un elemento
nombre.remove('Octavio')
print(nombre)

#eliminar el ultimo valor agregado 
nombre.pop()
print(nombre)

#eliminar un indice
del nombre[0]
print(nombre)

#limpiar la lista
nombre.clear()
print(nombre)

#eliminar la lista por completo 
#del nombre
print(nombre)