mi_lista=[10,20,30,40,50]

#Acceder a un elemento especifico de la lista

primer_elemento=mi_lista[0]
segundo_elemento=mi_lista[1]

#Acceder a elementos desde el final usando indices negativos

ultimo_elemento=mi_lista[-1]
penultimo_elemento=mi_lista[-2]

#Imprimir los resultados

# print(f"Primer Elemento {primer_elemento}")
# print(f"Segundo Elemento {segundo_elemento}")
# print(f"Ultimo Elemento {ultimo_elemento}")
# print(f"Penultimo Elemento {penultimo_elemento}")
"""
Extraer un rango de elementos de la lista(Sublista)
SLICING .-A la tecnica de extraer un subconjunto de elementos de una 
secuencia , lista , tupla o cadena
se debe utilizar el operador de ":"
Sintaxis:

secuencia[inicio:fin:paso]
"""
mi_lista=[10,20,30,40,50]
#sub_lista=mi_lista[1:4]  #1=Inclusive , #4=Exclusive
#print(sub_lista)

"""
obtener los elementos desde el principio hasta un indice especifico
"""
#primeros_tres_elementos=mi_lista[:3]
#print(primeros_tres_elementos)

"""
obtener los elementos desde un indice especifico hasta el final
"""
mi_lista=[10,20,30,40,50,80,90,100]
cadena="La Flor que sembre en mi jardin tomo en verano un color celeste"
#ultimo_dos_elementos=mi_lista[3:]
#print(ultimo_dos_elementos)
ultimo_dos_elementos=cadena[25:]
print(ultimo_dos_elementos)
