edad =int(input("Escribe tu edad de un rango de 0 a 30 años: "))
mensaje= None

if 0<= edad <=9:
    mensaje="La infancia es increible..."
elif 10<= edad <= 19:
    mensaje = "Muchos cambios y mucho estudio..."
elif 20 <= edad <=30:
    mensaje = "Amor y comienza el trabajo..."
else: 
    mensaje = "Etapa de vida no reconocida"

print(f'Tu edad es: {edad}, {mensaje}')