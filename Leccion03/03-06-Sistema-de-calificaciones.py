calificacion = float(input("Ingrese el valor del estduiante: "))
mensaje= None
if calificacion == 9 or calificacion == 10:
    mensaje="A"
elif 8<= calificacion < 9:
    mensaje= "B"
elif 7<= calificacion < 8:
    mensaje= "C"
elif 6<= calificacion < 7:
    mensaje= "D"
elif 0<= calificacion < 6:
    mensaje= "F"
else:
    mensaje = "Valor incorrecto"

print(f'La calificacion proporcionada es {calificacion}, {mensaje}')