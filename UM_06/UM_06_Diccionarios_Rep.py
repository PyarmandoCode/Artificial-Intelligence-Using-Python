mi_diccionario = {'nombre':'Juan','edad':25,'ciudad':'california'}

# print(mi_diccionario)
# print(mi_diccionario['nombre'])
# print(mi_diccionario['edad'])
# print(mi_diccionario['ciudad'])

"""
Agregar y actualizar elementos del diccionario
"""
mi_diccionario['ocupacion']='Programador'
mi_diccionario['nombre']='Jose'

"""
Eliminar elementos del diccionario por la clave
"""
del mi_diccionario['ocupacion']
#print(mi_diccionario)

"""
Obtener todas las claves
"""
claves = mi_diccionario.keys()

"""
Obtener todos los valores
"""
valores= mi_diccionario.values()

"""
Obtener claves y valores
"""
claves_valores=mi_diccionario.items()

"""
Verificar la existencia de una clave
"""

mi_diccionario = {'nombre':'Juan','edad':25,'ciudad':'california'}
existe_la_clave='nombre' in mi_diccionario

"""
Obtener un valor Predeterminado
"""
valor=mi_diccionario.get('altura','no existe el valor')
#print(valor)


"""
Diccionarios Anidados lo agregas A una lista
"""
usuarios = [
    {'nombre':'Juan','edad':25,'ciudad':'california'},
    {'nombre':'Arturo','edad':22,'ciudad':'new york'},
    {'nombre':'Pedro','edad':15,'ciudad':'texas'},
    {'nombre':'Miguel','edad':23,'ciudad':'california'},
    {'nombre':'Jose','edad':29,'ciudad':'california'},
]

size = len(usuarios)
print(size)












