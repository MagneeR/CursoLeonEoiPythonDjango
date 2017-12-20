""" Colores para la consola """

from colorama import init, Fore, Back, Style
init()

print('Hola')
print(Fore.BLUE, 'Soy una frase en azul') #Color de las palabras
print(Fore.CYAN, 'Soy una frase en cyan')
print(Fore.RED, 'Soy una frase en roja')
print(Back.GREEN + 'Fondo verde')
print(Style.RESET_ALL)
print(Fore.WHITE + 'Fondo normal y letras en blanco')