#imprimir numeros del 5 a 1 de manera descendente

def desendente(numeros):
    if numeros>=1:
        print(numeros)
        desendente(numeros-1)
    elif numeros == 0:
        return
    elif numeros<=0:
        print('Valor incorrecto...')

desendente(10)