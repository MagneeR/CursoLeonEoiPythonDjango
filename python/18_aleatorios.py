"""Generacion de numeros aleatorios"""

import random

#Vamos a generar 10 numeros aleatorios
for n in range(10):
    print('Entero aleatorio:', random.randint(0,10)) #Rango de randoms que quiero

#Random puro entre 0 y 1
for n in range(4):
    print(random.random()) #Muestra numeros decimales entre 0 y 1

L = ['Oscar', 'Ruben', 'Javi', 'Daniel', 'Marta', 'Raul']
#Elemento aleatorio de una lista
for n in range(8):
    print(random.choice(L)) #Coge un elemento aleatorio de la lista cada vez que da una vuelta

#Elementos aleatorios de la lista pero que se pueden repetir
r = random.choices(L, k = 2) #k es el numero de elementos que quiero coger de la lista que le paso
print(r)

#Cambiar el orden de los elementos de una lista de forma aleatoria
random.shuffle(L)
print(L)

#A partir de una lista crear otra con k elementos que no esten repetidos
print(random.sample(L, k = 2))
print(random.sample(L, k = 2))
print(random.sample(L, k = 2))
print(random.sample(L, k = 2))