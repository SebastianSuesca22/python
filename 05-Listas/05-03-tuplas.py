 #Definir una tupla

frutas =('Naranja','platano','Guayaba')
print(frutas)

#saber el largo 
print(len(frutas))

#acceder a un elemento 
print(frutas[0])

#navegacion inversa
print(frutas[-1])

#rango de valores
print(frutas[0:1]) #ultimo indice no se incluye

for fruta in frutas:
    print(fruta, end= ' ') #pára que no quede salto de linea 


#cambiar el valor tupla
#frutas[0]='Pera' #no se deja cambiar el valor


frutaLista = list(frutas)

frutaLista[0]='Pera'
frutas = tuple(frutaLista)
print('\n', frutas)
