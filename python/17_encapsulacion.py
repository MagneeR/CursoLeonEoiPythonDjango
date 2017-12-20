"""Encapsulacion en python"""

class MyCounter:
    __secretCount = 0
    def count(self):
        self.__internal_count()
        print(self.__secretCount)
    def __internal_count(self):
        self.__secretCount += 1

counter = MyCounter()
counter.count()
counter.count()
print(counter.__secretCount)
#Si yo no quiero que nadie sepa que hay en mi clase tendre que poner __nombreVariableAEsconder
#Al hacer esto, el print no funciona porque no encuentra la variable
counter.__internal_count() #Esta linea tambien dara fallo por las __ del metodo