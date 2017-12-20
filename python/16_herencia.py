"""Herencia de clases"""

class Vehicle:
    def __init__(self):
        self.wheels = 0
        #Con esto me dara el nombre de la instancia actual(Car o Plane)
        self.name = self.__class__.__name__
        print('Constructor de', self.name)

    def move(self):
        return 'Moving'

class Car(Vehicle): #Al meter la clase padre entre parentesis, esta hereda las propiedades del padre
    def __init__(self):
        super().__init__()#Estoy llamando a la clase madre
        self.wheels = 4
    
    def move(self):
        return 'Moving on the road'


class Plane(Vehicle):
    def __init__(self):
        super().__init__()#Estoy llamando a la clase madre
        self.wheels = 2

    def move(self):
        return 'Flying' 


VEHICLES = (Vehicle(), Car(), Plane())

#Loop sobre el array de vehicles
for v in VEHICLES:
    print('{} tiene {} ruedas y se mueve así: {}'\
    .format(v.name, v.wheels, v.move()))

#Herencia multiple
class A:
    def fly(self):
        print('Flying')

class B:
    def run(self):
        print('Running')

class C(A, B): #La clase C hereda los metodos de las clases A y B
    def eat(self):
        print('Eating')

c = C()
c.eat()
c.fly()
c.run()