"""Funciones simples en Python"""

#Una funcion se crea con la palabra def

def hi():#inicio de la funcion
    print('Holii')
#fin de la funcion porque estoy escribiendo al mismo nivel que el inicio de la funcion
hi() #Llamo a la funcion

def say_hi(name):
    print('Hi',name)
say_hi('Raúl')

#Funcion con dos parametros
def add_name(name_list, name):
    name_list.append(name)
    print(name_list)

l = ['Vayne', 'Jinx']
add_name(l, 'Lucian')

#Modificar argumento dentro de la funcion
def talk(word):
    word = 'No pongo lo que tu dices porque no me da la gana'
    print(word)
talk('Hola')