""" Ejemplos para trabajar con cadenas de texto"""

TEXTO = 'hello world' #una cadena es un array de caracteres
print(TEXTO[0])
print(TEXTO[1])
print(TEXTO[2])
print(TEXTO[3])
print(TEXTO[4])

print(TEXTO[5:8]) #me imprime del caracter 5 al 8 de la variable TEXTO sin incluir el
                    #caracter en la posicion 8
print(TEXTO[6:]) #me imprime desde el caracter 6 hasta el final
print(TEXTO[:3]) #me imprime desde el caracter 0 hasta el 3 sin incluirlo

print(TEXTO + ' ' + TEXTO) #Concatenacion de strings

print(TEXTO.upper()) #upper() me convierte texto a mayusculas
print(TEXTO.capitalize()) #capitalize() pone la primera letra en mayusculas
print(len(TEXTO)) #numero de caracteres de TEXTO
print(TEXTO.split()) #crea un array usando el espacio en blanco
print(TEXTO.split('lo')) #decimos a partir de donde queremos separar el string