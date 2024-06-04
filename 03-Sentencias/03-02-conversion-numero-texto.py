numero = int(input("Proporciona un valor entre 1 y 3: "))

if numero == 1:
    numeroTexto = 'Numero uno'
elif numero == 2:
    numeroTexto = 'Numero dos'
elif numero == 3:
    numeroTexto = 'Numero tres'
else: 
    numeroTexto = 'Fuera de rango '

print(f'Numero proporcionad: {numero}: {numeroTexto}')    