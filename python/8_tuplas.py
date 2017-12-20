"""Una tupla es como una lista pero con parentesis
Diferencia basica entre lista y tupla es que las tuplas no se pueden modificar,
es decir, es un objeto inmutable. Ocupa menos memoria que una lista
Las tuplas son exclusivas de Python
"""
#Para buscar dentro de las tuplas si que debemos usar corchetes
TUP = (1, 2, 3, 4, 5, "seis") 
print(TUP)
print(TUP[0]) #Asi muestra lo que hay en la posicion que le de
print(TUP[4])
print(TUP[2:5]) #Muestro los valores desde la posicion 2 hasta la 5 sin incluirla
                 #pero se ve como un array
print(TUP[:3])
print(TUP[2:])

size = len(TUP) 
print('Tamaño de la lista:', size)

#Concatenar dos listas
LIST2 = ('siete', 8 , True, False)
TUP += LIST2
print(TUP)

SUMA = (3 + 2) - 1
TUPLA2 = (3,) #Tupla de un solo elemento
#Para diferenciar entre numeros y tuplas de un solo numero hay que poner, 
#despues del elemento
print(type(TUPLA2))