edadAdulto = 18

edadPersona = int(input('Ingresa la edad de la persona: '))

if  edadPersona >= edadAdulto:
    print(f'La persona con edad {edadPersona} es un adulto')
else:
    print(f'La persona con edad {edadPersona} es menor de edad')