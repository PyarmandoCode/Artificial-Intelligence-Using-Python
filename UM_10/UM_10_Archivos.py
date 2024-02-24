import csv
"""
Lectura y Escritura de Archivos CSV
con=0
with open('./UM_10/archivos/productos.csv','r') as file:
    reader= csv.reader(file)
    for row in reader:
        print(f"Fila {con} - {row}")
        con +=1

"""
"""
Escribir en el Archivo
def generar_archivo():
    try:
        data_to_write = [['CODIGO','PRODUCTO','STOCK'],
                        ['A100','XYZ',200],
                        ['A200','MNO',300],
                        ['A400','LXO',500]
                        ] 
        with open('nuevos_datos.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_to_write)
    except Exception as err:
        print(f"El Archivo no se genero {err}")        
    else:
        print("Se genero el archivo correctamente")    
    finally:
        #'nuevos_datos.close'    
        file.close()
generar_archivo()        

"""

