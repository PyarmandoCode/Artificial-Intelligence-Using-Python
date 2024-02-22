"""
Este módulo proporciona acceso a las funciones matemáticas
import math

import math
math.pi
math.cos(math.pi/4)
res=math.sqrt(20)
print(res)
"""

"""
Modulo de estadisticas
import statistics
datos=[2.90,10.5,14.7,23.7,10.5]
media_aritmetica=statistics.mean(datos) #media aritmetica("Promedio")
valor_medio=statistics.median(datos) #Valor medio
variance=statistics.variance(datos) #La Variance
valor_moda=statistics.mode(datos)#La Moda de la lista de datos
"""
from datetime import datetime,timedelta

# Obtener la fecha y la hora del actual
fecha_actual=datetime.now()
#print(fecha_actual)

#Acceder a los componentes de la fecha
# print("Año",fecha_actual.year)
# print("Año",fecha_actual.month)
# print("Año",fecha_actual.day)
# print("Año",fecha_actual.hour)
# print("Año",fecha_actual.minute)
# print("Año",fecha_actual.second)

#Operaciones entre fechas
nueva_fecha=fecha_actual+timedelta(days=7)
#print(nueva_fecha)

#Conversion de fechas
cadena_fecha="2023-08-25"
fecha_desde_cadena=datetime.strptime(cadena_fecha,"%Y-%m-%d")
#print(f"fecha desde cadena {fecha_desde_cadena}")

fecha1 = datetime(2022,5,10)
fecha2 = datetime(2022,3,15)

#Calcular la diferencia entre las dos fechas
diferencia_entre_fecha=fecha1-fecha2
print(f"diferencia entre dias {diferencia_entre_fecha.days}")

diferencia_entre_años=diferencia_entre_fecha.days//365
diferencia_entre_meses=(diferencia_entre_fecha.days % 365) //30

import csv

#print(diferencia_entre_fecha)


# class Persona:
#     def __init__(self,nombre,apellido):
#         self.nombre=nombre
#         self.apellido=apellido
#     def __str__(self):
#         return self.apellido
    

# persona1=Persona("Armando","Ruiz")
# persona2=Persona("Jose","Ruiz")
# persona3=Persona("Lopez","Ruiz")
# persona4=Persona("Juan","Ruiz")
# print(persona4)






        












