# n=int(input("Ingrese un Numero:")) # 10
# suma=0 #Acumulador
# con=0
# for x in range(1,n+1):
#     suma=suma+x
#     con +=1
# promedio = suma/con    
# print(f"La Cantidad de elementos del bucle es {con} ")    
# print(f"La Suma de los valores es {suma}")
# print(f"El Promedio es {promedio}")

"""
Ingrese 3 notas de un estudiante y calcule su promedio

suma=0
for x in range(1,3+1):
    nota=float(input(f"Ingrese la nota {x}:"))
    suma=suma+nota
promedio=suma/3
if promedio>10.5:
    print(f"El Estudiante Aprobo el curso con {round(promedio,2)}")
else:
    print(f"El Estudiante Desaprobo el curso con {round(promedio,2)}") 
"""

"""
Crear un script que me permita ejecutar un bucle indefinidamente hasta que
el usuario ingrese "n"

while True:
    respuesta=input("¿Desea Continuar?(S/N):")
    if respuesta=='s':
        nota=int(input("Ingrese una Nota:"))
    else:
        print("Saliendo del programa")    
        break#Sale del Bucle While
"""

"""
Simular una compra en un supermercado de "n" productos cuando escriba "fin"
dejare de comprar y me debera mostrar el total a pagar

total_compra=0
while True:
    producto=input("Ingrese el nombre del producto(o 'fin' para salir)")
    if producto =='fin':
        break
    cantidad=int(input(f"Ingrese la cantidad del producto {producto}:"))
    precio=float(input(f"Ingrese el precio del producto {producto}:"))
    subtotal = cantidad* precio
    total_compra +=subtotal #acumular todas los subtotales de los productos comprados
print(f"Total de la compra ${total_compra}")
"""
"""
Buscar un un elemento en una lista
"""
lista=["gaseosa","panecillo","galleta","snack"]
prod_bus=input("Ingrese el producto a buscar:")

for producto in lista:
    if producto==prod_bus.lower():#lower que convierte a minuscula
        print(f"Se encontro {producto} en la lista")
        break
else:
    print(f"{prod_bus} no se encuentra en la lista")


# frase="EL GRAN ELEFANTE BLANCO"
# print(frase.upper())

    











    
   
 


   



