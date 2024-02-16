"""
TIP DEL DIA

from datetime import datetime
fecha_hora_actual=datetime.now()
#print(fecha_hora_actual)

import keyword
print(keyword.kwlist)

import keyword
print(keyword.kwlist) #modulo
from keyword import kwlist #importas una parte del modulo

import math
import statistics
import random

"""
"""
Input.-Ingresar datos por consola
{}=Las Llaves son para imprimir el contenido de ua variable

curso=input("Ingrese el nombre del curso:")
costo=float(input("Ingrese el Costo del curso:"))
unidades=int(input("Ingrese las vacantes:"))
total = costo * unidades
print(f"El Total del Curso de {curso} es {total}")
#print(type(curso))
#print(type(costo))
"""

"""
Realizar un Script que me permita visualizar la cantida que debo pagar por una
compra en un SUPER
"""
producto =input("Ingrese el Producto a comprar:")
precio = float(input("Ingrese el Precio del Producto:"))
unidades = int(input("Ingrese las Unidades a comprar:"))
subtotal= precio*unidades
print(f"La Cantidad a pagar por el  producto {producto} es {subtotal:.3f}")
print(f"La Cantidad a pagar por el  producto {producto} es {round(subtotal,2)}")













