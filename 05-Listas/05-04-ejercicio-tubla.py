tupla =(13, 1, 8, 3, 2, 5, 8)

lista=[]
#filtrando elementos menores a 5 
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

print(lista)