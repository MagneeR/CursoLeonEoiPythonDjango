"""Ejemplos de excepciones """
from libs.urlloader import load_url
from urllib.error import HTTPError #Este es el error que querremos ver

try:
    raise Exception('Esto no funciona ni con dinero') #Genero una excepcion para que falle y vaya a except
    print('¿Funcionará?')
except Exception as error:#Indico el tipo de excepcion que quiero recibir
    print('Ha fallado', error) #Muestro el error que obtengo
                                #repr(error) => da mas info sobre el error

#Quiero capturar el error concreto que me de
try:
    load_url('https://swapi.co/api/peo')
except HTTPError as err:
    print('Error al cargar la URL:',repr(err))