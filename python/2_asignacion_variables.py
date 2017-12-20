TEXTO = 'Esto es un texto de una linea'
print(TEXTO)
print(type(TEXTO))

NUMERO_SIMPLE = 4 #el tipo de numero sera por defecto int
print(NUMERO_SIMPLE)
print(type(NUMERO_SIMPLE))

NUMERO_FLOAT = 100.4
print(NUMERO_FLOAT)
print(type(NUMERO_FLOAT))#con type y la variable te dice el tipo de variable que es

#snake_case es la forma de escribir variables en python, van separadas con _
MAYOR_DE_EDAD = True #Cuando es un booleano hay que escribir la primera en mayuscula
print(MAYOR_DE_EDAD)
print(type(MAYOR_DE_EDAD))

PARRAFO = """Esto es 
un string con 
varias lineas"""
print(PARRAFO)
print(type(PARRAFO))

NOMBRE = 'Raúl'
EDAD = 23
print('{} tiene {} años'.format(NOMBRE,EDAD))

A = B = C = 7 #Asigno un mismo valor a 3 variables distintas
print(A)
print(B)
print(C)

D, F, G = 1, False, 'Palabra' #Doy diferentes valores a diferentes variables a la vez
print(D)
print(F)
print(G)