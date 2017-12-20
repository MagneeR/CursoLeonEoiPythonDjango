"""Trabajando con fechas y hora"""

import time #Libreria estandar de python que da la hora

seconds = time.time()
print('Número de ticks desde las 12:00 del 1 de enero de 1970',seconds)
#Tick es un intervalo de tiempo que tiene el origen a las 12:00 del 1 de enero de 1970

#Hora local
local_time = time.localtime(seconds)
print(local_time)
print(type(local_time))

#Hora local formateada, vista de forma mas normal
asctime = time.asctime(local_time)
print(asctime)

#Hora con formato personalizado
date_format = '%d-%b-%Y a las %H:%M:%S'
date_formatted = time.strftime(date_format, time.gmtime(seconds))

print(date_formatted)