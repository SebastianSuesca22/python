nombre = str(input("Ingrese el nombre del libro: "))
id = int(input("Ingrese el ID del libro: "))
precio = float(input("Ingrese el valor del libro: "))
envio = bool(input("Tiene envio gratis? True/False: "))

if envio =='True':
    envio == True
elif envio == 'False':
    envio == False
else:
    envio == 'Valor incorrecto, debe escribir entre True/False'

print(f'''
    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    Envio gratituo: {envio}
''')