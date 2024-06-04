#factorial de 5

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
    
resultado = factorial(int(input("Ingrese un numero: ")))

print(f'el factorial es {resultado}')