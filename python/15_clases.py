"""Clases en python"""

class Thing:
    pass

thing = Thing() #Instancia de la clase Thing creada

#Constructor sin argumentos o parametros
class Fruit:
    #Metodo del constructor de python
    def __init__(self): #Siempre sera asi
        print('Objeto fruta')

fruit = Fruit()

#Argumentos del constructor
class CustomFruit:
    """Esta clase no vale para mucho pero me gusta escribir comentarios"""
    #Voy a crear una propiedad estatica, que afectara a todos los objetos que creemos con esta clase
    COUNTER = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.juices = 0
        #Voy a acceder a COUNTER y hacer que aumente cada vez que la llame
        CustomFruit.COUNTER += 1

    def __str__(self): #Hace que un objeto se muestre como un string
        return 'Soy una fruta, me llamo {} y mi color es {}.\nHay una {} frutas en total'\
        .format(self.name, self.color, CustomFruit.COUNTER) #La barra \ nos deja colocar una sentencia en dos lineas

    def make_juice(self, count):
        #Por el numero de veces que quiera hacer zumo imprimo que quiero hacer zumo
        for n in range(count): #Pasa una vez por cada numero
            print('Haciendo zumo de ', self.name)
            self.juices += 1


custom = CustomFruit('Pera', 'verde')
print(custom)
custom.make_juice(2)
print('Zumos hechos:' ,custom.juices)

custom2 = CustomFruit('Kiwi', 'marron')
print(custom2)
custom2.make_juice(4)
print('Zumos hechos:' ,custom2.juices)