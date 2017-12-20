"""Ejemplo del uso de expresiones regulares"""

import re #Libreria de python de expresiones regulares

phone = '54434378543274 #esto es un numero de telefono'
#He mezclado un string con un comentario de python
#Ahora voy a borrar el comentario de phone
number = re.sub(r'#.*$', '', phone)#Con esta expresion me cogera desde la almohadilla hasta el final, 
                                #seria el patron de busqueda
                                #El siguiente parametro seria por que lo quiero sustituir
                                #El ultimo parametro seria de donde lo quiero buscar
print('Telefono:', number)

#Borrar cualquier cosa que no sean digitos
number = re.sub(r'\D', '', phone) #r'\D' => Con esto le digo que coja todo lo que no sea un digito
print('Telefono:', number)