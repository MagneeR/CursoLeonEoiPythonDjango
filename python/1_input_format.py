"""Ejemplo para pedir input del usuario y formatear la respuesta"""
#variable en mayusculas porque esta fuera de una funcion y es asi por convencion
PREGUNTA = '¿Como te llamas? '
RESPUESTA = input(PREGUNTA)

print('Hola', RESPUESTA, '¿como estas?')

respuesta_formateada = 'Hola {}, ¿como estas?'.format(RESPUESTA)
#Es otra forma de hacer el print de arriba. Entre las llaves escribira las variables 
# que pongamos en format separadas por comas
print(respuesta_formateada)