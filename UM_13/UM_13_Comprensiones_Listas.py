"""
(List Comprehsion)es una caracteristica de Python que proporciona una forma
concisa de crear listas.
permite crear listas de una manera mas compacta y legible en comparacion
con los bucles tradicinales.
"""

"""
Crear Una Lista de los cuadrados de los primeros 5 numertos
"""
"""
Manera Tradicional
lista=list()
for x in range(1,6):
    valor=x**2
    lista.append(valor)
print(f"Esta es la lista de Cuadrados {lista}")    
"""
cuadrados=[x**2 for x in range(1,6)]
#print(type(cuadrados))
#print(f"Esta es la lista de Cuadrados {cuadrados}")    

"""
Crear una Lista de los cuadrados de los numeros pares entre 1 y 10
"""
solo_pares=[x**2 for x in range(1,11) if x % 2 ==0 ]

# lista_valores=list()
# for x in range(1,11):
#     valor=x**2
#     if valor % 2 ==0:
#         lista_valores.append(valor)
# print(f"Esta es la lista de Cuadrados {lista_valores}")    
#print(solo_pares)

"""
Crear una Lista de palabras en mayusculas a partir de una lista de palabras
"""
words=['python','es','genial']
uppercase_words=[word.upper() for word in words]
#print(uppercase_words)

#Enumeracion = Enumerate obtener el indice de cada elemento de la lista

#words=['python','es','genial']
result=[(index,word) for index,word in enumerate(words)]
print(result)
# for index,word in enumerate(words):
#    print (f"{index} - {word}")









