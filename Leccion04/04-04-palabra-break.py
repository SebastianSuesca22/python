for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin ciclo for')

#imprimir los numeros pares del 1 al 100
contador = 0

while contador <=100:
    contador +=1
    if contador % 2 == 0:
        print(contador)