"""Bucles en Python con funciones"""
"""
def print_everything(*args):
    for n in args: #for laVariableQueQuieraUsar in loQueQuieroRecorrer
        print(n)

print_everything('manzana', 'platano', 'kiwi')

def print_all_with_position(*args):
    for count, thing in enumerate(args): #count, thing serian cada uno una tupla
        print('{}.{}'.format(count,thing)) #Forma mas bonita
        #Forma normal:print(count,thing) 
    #print(enumerate(args))
#Enumerate coge cada valor de args y los asigna a la variable thing; y en count se guarda la posicion
#de cada arg
print_all_with_position('manzana', 'platano', 'kiwi')

#Bucle While
counter = 0
while True:
    counter += 1
    print(counter)
    if counter >= 3:
        break
print('fin del while')

def count_until(n=3):
    counter = 0
    while counter <= n:
        print(counter)
        counter += 1

count_until(30)
"""
def show_keyword_arguments(**kwargs):
    for name, value in kwargs.items():
        print('{}: {}'.format(name, value))
show_keyword_arguments(uno = 1, dos = 2, nombre = 'Raúl')