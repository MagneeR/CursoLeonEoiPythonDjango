"""Los diccionarios de Python son muy parecidos a los objetos de JS
Se escriben como los JSON
"""

ALUMNO = {
    'nombre': 'Raúl',
    'edad' : '23',
    'clase' : 'Phyton'
} 

#Quiero ver el nombre del alumno
print(ALUMNO)
print(ALUMNO['nombre']) #Le paso el nombre de la propiedad que quiero saber como array
print(ALUMNO['edad'])
print(ALUMNO['clase'])
print('Nombre del alumno: ' + ALUMNO['nombre'] + '\n' + 'Edad del alumno: ' + ALUMNO['edad'] + '\n' +
'Esta en clase de: ' + ALUMNO['clase'])

ALUMNO['edad'] = 22 #Modifico el valor de una propiedad existente
print(ALUMNO)

ALUMNO['sexo'] = 'Masculino' #Añado una propiedad nueva al diccionario
print(ALUMNO)

del ALUMNO['sexo'] #Borro una propiedad del diccionario
print(ALUMNO)

#Metodo del diccionario que borra todas las propiedades del diccionario que queramos: clear
#Tambien puedo borrar el diccionario entero con del
ALUMNO.clear()
print(ALUMNO)

