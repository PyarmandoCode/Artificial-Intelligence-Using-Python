"""
Utilice el Bucle for cuando conozca las veces
que se repetira el proceso
"""

#for i in range(5,10,2):
#    print(f"{i} Bienvenido al Curso de Python con IA")

"""
Si encuentra un Numero Impar debe terminar el bucle
"""
# numeros=[2,4,1,6,8,9,10]    
# for numero in numeros:
#     if numero % 2 != 0:
#         print("Se encontro un Numero Impar. Terminando el Bucle")
#         break # Interrumpe la ejecuccion del Bucle
#     print(numero)

"""
Si encuentro numeros impares voy a saltarlos
"""
numeros=[1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    if numero % 2 !=0:
        #print("Se encontro un numero impar")
        continue
    print(numero)
