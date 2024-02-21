import sys
import random

def mi_funcion():
    try:
        resultado=10 /0
        print("Este ecodigo no se ejecutara por la excepcion")
    except ZeroDivisionError:
        #Manejar la excepcion y salir dela funcion o del programa
        sys.exit() 

#mi_funcion()           

cursos = ["PYTHON","IA","BD"]
alea= random.randrange(1,10)        
azar= random.choices(cursos)
print(azar)

