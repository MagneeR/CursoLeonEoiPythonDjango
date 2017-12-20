"""Libreria que voy a reutilizar"""

from libs import urlloader
from urllib.error import HTTPError
import json

class Swapi:
    base_url = 'https://swapi.co/api/'
    #Si cacheo el metodo no tengo que estar haciendo peticiones todo el rato
    __people = None

    def __get_results(self, resource):
        try:
            api_result = urlloader.load_url(self.base_url + resource) #Cargo una url
            result_json = json.loads(api_result) #Lo que recibo lo convierto en JSON
            return result_json['results'] #Muestro results
        except HTTPError as error:
            print('Error al cargar la URL', repr(error))
            return None #Es el null de python
        except Exception as ex:
            print('Error generico:', repr(ex))
            return None

    def get_people(self):
        #Otra forma
        if self.__people:
            return self.__people

        results = self.__get_results('people/')
        self.__people = [(person['name'], person['gender']) for person in results]
        return self.__people
        """
        results = self.__get_results('people/')
        return [] if results is None \
        else [(person['name'], person['gender']) for person in results]
        #Forma aun mas reducida de hacer lo mismo
        """
        """
        if results is None:
            return []
        else:
            return[(person['name'], person['gender']) for person in results]  #Manera reducida de hacer lo de abajo
        """
        """
            people_data = []
            for person in result:
                person_data = {'name' : person['name'], 'gender' : person['gender']}
                people_data.append(person_data)
            return people_data
        """
