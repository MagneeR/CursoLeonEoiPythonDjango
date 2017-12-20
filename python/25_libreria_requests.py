""" La libreria request simplifica mucho el trabajo con llamadas
y repuestas HTTP"""

"""Esta libreria no esta por defecto en python, se instala desde fuera
Lo que instale se guardara en el interprete de python. Para aislar librerias entre proyectos distintos
y evitar borrarlas hay que crear un virtual enviroment(Copia del interprete de python) y asignarlo a 
cada proyecto para evitar mezclar librerias
Comando que usare para instalarla => pip install requests ==version
Para solucionar todos estos problemas => pipenv para crear el entorno
"""
import requests

response = requests.get('https://httpbin.org/ip')
#Esta libreria lee JSONS sin tener que importar otra libreria
ip = response.json()['origin']
print('Tu IP es: ', ip)

response = requests.get('https://swapi.co/api/people/')
people = response.json()['results']
for person in people:
    print(person['name'])
