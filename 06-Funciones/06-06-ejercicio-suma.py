def suma_valores(*args):
    resultado=0
    for valor in args:
        resultado +=valor
    return resultado

print(suma_valores(3,5,9,4,6))