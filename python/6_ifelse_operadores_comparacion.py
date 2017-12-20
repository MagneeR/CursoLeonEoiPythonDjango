"""Operadores de comparacion"""

a, b, c = 21, 10, 0
if a == b: #¡¡¡¡¡¡¡¡¡¡¡¡¡MUUUY IMPORTANTE LAS TABULACIONES!!!!!!!!!!!!!!!!!!
    print('a es igual b')
else:
    print('a no es igual que b')

if a != b:
    print('a no es igual a b')
else:
    print('a es igual que b')

print(a < b) #booleano
print(a > b)

if a <= b:
    print('a es menor o igual que b')
else:
    print('a no es menor o igual que b')
print(a >= b)

print(a is b) #exclusivo de python
print(a is a) #exclusivo de python
print(a is not b) #exclusivo de python