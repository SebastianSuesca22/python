import random

for numero in range(1, 100):
    # numero = random.randint(1,100)
    if numero %2 == 0:
        print(f'Numero par: {numero}')
    else:
        print(f'Numero impar: {numero}')