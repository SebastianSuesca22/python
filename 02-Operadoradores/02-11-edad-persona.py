edad = int(input('Introduce tu edad: '))

veintes = edad >= 20 and edad <30
print(veintes)
treintas = edad >=30 and edad <40
print(treintas)


if veintes or treintas:
    print('Dentro de rango (20\'s) o (30\'s)')
    if veintes:
        print("Dentro de los 20's")
    elif treintas:
        print("Dentro de los 30's")
else:
    print("No esta dentro de los 20's o 30 's")


