"""
Crear un Archivo en Formato CSV , con datos provenientes de una lista
sumar los datos numericos y colocarlo en la ultima fila del CSV
"""
import csv
import gc

#Recollecion de Basura
gc.collect()

#Definir el nombre del archivo
nombre_archivo='datos.csv'
#Crear datos de ejemplo
datos =[
    ['NOMBRE','EDAD'],
    ['JUAN',25],
    ['MARIA',19],
    ['PEDRO',45],
    ['ARMANDO',43]
]

#Suma la columna edad
total_edades = sum(row[1] for row in datos[1:]) #Operadores Ternarios

#Especificar la fila en la que se colocara em total
fila_total=len(datos) -1#4

#Calculando el promedio de edades
promedio_edades=total_edades/fila_total

#Anadir el total a la ultima fila de datos
datos.append(['TOTAL',total_edades])
datos.append(['PROMEDIO DE EDADES',promedio_edades])

#Escribir datos en el archivo CSV
with open(nombre_archivo,'w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(datos)

#Mostrar los datos escritos en el archivo
with open (nombre_archivo,'r')as file:
    reader=csv.reader(file)    
    for row in reader:
        print(row)
    
        