"""Esto es un ejercicio pero quiero tener una libreria para usarla en cualquier sitio"""

from libs import swapi_client

client = swapi_client.Swapi()
people = client.get_people()
people = client.get_people()
print(people)