"""
Leer Archivo

import csv
con=0
with open('productos.csv') as archivo_csv:
    lector_csv=csv.reader(archivo_csv)
    #iterar sobre las filas del archivo
    for fila in lector_csv:
        if con>0:
            print(fila)
        con +=1
    print(con)
"""

with open('ejemplo.txt') as file:
    contenido=file.read()
    print(contenido)
    
    #iterar sobre las filas del archivo


# import openpyxl
# archivo_xlsx=openpyxl.load_workbook("productos.xlsx")
# hoja_trabajo=archivo_xlsx["productos"]
# for fila in hoja_trabajo.iter_rows(values_only=True):
#     print(fila)






