"""Ejemplos para trabajar con listas
ctrl+f2 sobre un nombre me deja cambiar ese nombre en todo el documento
"""

#En minuscula no se puede poner list porque es una palabra reservada de python
LIST = [1, 2, 3, 4, 5, "seis"] #Las listas son como arrays y en la consola se ve como array
print(LIST)
print(LIST[0]) #Asi muestra lo que hay en la posicion que le de
print(LIST[4])
print(LIST[2:5]) #Muestro los valores desde la posicion 2 hasta la 5 sin incluirla
                 #pero se ve como un array
print(LIST[:3])
print(LIST[2:])

size = len(LIST) 
print('Tamaño de la lista:', size)

del LIST[2] #Borro el elemento de la lista que yo diga
print(LIST)

LIST[2] = 'tres' #Modifico un valor de la lista
print(LIST)

#Concatenar dos listas
LIST2 = ['siete', 8 , True, False]
LIST += LIST2
print(LIST)

#Añadir elemento a la lista
LIST.append('elemento nuevo')
print(LIST)

LIST.remove('seis') #Borro un elemento segun su valor
print(LIST)

LIST.reverse() #Da la vuelta a la lista (lo del final al principio)
print(LIST)

LIST.insert(1, 'PC') #Crea un elemento que yo le pase en la posicion que elija
                    #insert(posicion en la que quiero meter el valor, valor que quiero añadir)
print(LIST)