"""
sets(Conjuntos)
-Es una coleccion no ordenada de elemento unicos e inmutables
-Se utiliza para almacenar elementos sin duplicados
-El Orden de los elementos no importa
-Son representados por llaves
-Y Trabajan como el las matematicas
-Los SET no admiten la indexacion
"""
conjunto_vacio= set() #constructor
conjunto_vacio={8,2,5,6}
conjunto_vacio.add(1) #Insertando un nuevo elemento
conjunto_vacio.add(34) #Insertando un nuevo elemento
conjunto_vacio.add(12) #Insertando un nuevo elemento
conjunto_vacio.remove(8)#Eliminando por el elemento no por el indice

#Buscar un elemento en un set
#valor=int(input("Ingrese el valor a buscar del conjunto:"))
#resultado= valor in conjunto_vacio
#print(resultado)#Devuelve un valor Booleano si el elemento se encontro

#print(conjunto_vacio)
#conjunto_vacio.remove(2)#Eliminar un elemento 

conjunto1 = {8,2,3,5,6,9} #{"Hugo","Pablo","Juan"} #Autos
conjunto2 = {12,3,5,7,1,11}#{"Maria","Pablo","Ernesto"}#Bicicletas

union_conjuntos= conjunto1.union(conjunto2) #Union de conjuntos
interseccion_conjuntos=conjunto1.intersection(conjunto2)#Que son comunes en ambos
es_sub_conjuntos=conjunto1.difference(conjunto2)#Devuelve los elementos presentes en el primer con junto pero no en el segundo

conjunto3={1,2,3,4,5}
conjunto4={3,4,5,6,7}

diferencia=conjunto3.difference(conjunto4)
interr=conjunto3.intersection(conjunto4)
print(interr) #


