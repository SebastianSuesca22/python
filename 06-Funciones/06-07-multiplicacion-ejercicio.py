def multiplicacion(*args):
    resultado=1
    for valor in args:
        resultado *= valor
    return  resultado

print(f'la multiplicacion es: {multiplicacion(2, 2, 4)}')