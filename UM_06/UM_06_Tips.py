#asignacion multiple
edad,nombre,altura,es_estudiante=25,"Armando",1.60,True
#asignar el mismo valor a varias variables
x = y = z = 10
frase1="Bienvenido " 
frase2="Curso de Python"
#print("Bienvenido " , " Curso de Python" ," 2024" ,sep='&')
# print("Bienvenido " ,end="")
# print("Al curso de Python " ,end="" )
# print("Con Inteligencia Artificial")
#print("\t\t Bienvenido \n\n al curso de python")
#print("Curso de Python Profesional con \"IA\" ")

"""
Tipo de Errores
-Error de Sintaxis(Syntaxis Errors)
-Error en tiempo de Ejecucion (Runtime Errors)
-Error Semanticos (Semantic Errors)
-Error Excepciones (Exceptions)
"""

resultado = 10 / 0

lista=[12,5,23,56]

# def calcular_promedio(lista):
#     suma=0
#     for numero in lista:
#         suma = suma * numero
#     promedio= suma /len(lista)    
#     return promedio

try:
    resultado = 12 / 0
except Exception as err:
    print(f"Ocurrio un Error {err}")    