mes = int(input("Proporciona el mes del año (1-12): "))

estacion = None 

if 1<= mes <=2 or mes ==12:
    estacion =  "Invierno"
elif 3<= mes <=5:
    estacion =  "Primavera"
elif 6<=  mes <= 8:
    estacion =  "Verano"
elif 9<= mes <=11:
    estacion = "Otoño"
else:
    estacion= "Mes no valido "

print(f'Para el mes {mes} la estacion es: {estacion}')
