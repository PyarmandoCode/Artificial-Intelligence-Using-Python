"""
Funciones para el Manejo de Strings
"""
cadena="Hola Mundo"

# for letra in cadena:
#     print(letra)

longitud=len(cadena) #Averiguar el tamaño de la cadena
#print(longitud)

cadena="hola Mundo"
mayusculas=cadena.upper() #Convierte la cadena a mayusculas
minusculas=cadena.lower() #Convierte la cadena a minusculas
tipo_titulo=cadena.capitalize()#Convierte la primera letra en mayusculas
tipo_titulo2=cadena.title()

#print(f"La cadena en mayusculas {mayusculas} en minusculas {minusculas} y de tipo titulo {tipo_titulo2}")

cadena="Hola,hola,hola,mundo!"
cuenta=cadena.count("hola")#Cuenta cuantas veces aparece una subcadena en la cadena principal
#print(f"Las Veces que aparecio hola en la cadena fueron {cuenta}")

cadena="Hola, mundo!"
posicion=cadena.find("mundo")#Encuentra la posicion de una subcadena
#print(f"La posicion donde se encuenta la cadena mundo es {posicion}")

cadena="Hola, mundo!"
nueva_cadena=cadena.replace("mundo","Python")#Reeemplaza todas las ocurrecnias de una subcadena a otra
#print(f"La Nueva cadena es {nueva_cadena}")

cadena="Hola, mundo!"
palabras=cadena.split(", ") #Divide la cadena en una lista de subcadenas usando el separador especifico
print(palabras)

cadena="  Hola, mundo!  "
sin_espacios=cadena.strip() #strip() , lstrip() ,rstrip() Elimina espacios en la cadena en los lados , en la izquierda y en la derecha
#print(sin_espacios)
























