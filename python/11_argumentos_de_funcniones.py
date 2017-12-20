"""Ejemplos de argumentos de funciones en Python
Diferentes maneras de usar argumentos
"""

#Argumentos posicionales obligatorios, es decir, que la funcion no funciona
#si no le paso name
def hi(name):
    print('Hi', name)
#asi falla => hi()

#Valores por defecto del argumento
def f(n = 'uno'):
    print(n)
f() #Ahora si funcionara porque el argumento tiene un valor

def f2(one, two, three = 3):
    print('one: ',one, ', two: ', two, ', three: ', three)
#Usar argumentos por orden
f2(45, 10, 22) #El 22 es un argumento opcional porque three ya tiene un valor

#Usar argumentos como keywords (palabras clave)
f2(three = 89, two = 90, one = 23) #Pongo el nombre del argumento y el valor que le quiero dar 
                        #y no tengo que pasar los argumentos por orden si no quiero

def dime_cosas(*args):#Con esto soy yo el que elijo que parametros le voy a pasar a la funcion
    print(args)
dime_cosas(20, 30, 90, True, False, 'Hola') #Me ha creado una tupla

def f3(name, *args):#Le paso un argumento obligatorio y otros opcionales
    print('Hola ',name)
    print(args)
TUPLA = ('Raúl',20, 30, 90, True, False, 'Hola')
f3('Raúl',*TUPLA)#Si no pusieramos el * no funcionaria

def f4(**kwars): #**kwars significa keyword arguments. Devolveria un diccionario
    print(kwars)
f4(cosa = 'PC', b = 'tres') #Devuelve un diccionario con las claves cosa y b que tendran esos valores
diccionario = {
    'c': 'uno',
    'b' : 'dos',
    'f' : True
}
#Asi petaria => f4(diccionario)
f4(**diccionario) #Asi ya estaria bien

