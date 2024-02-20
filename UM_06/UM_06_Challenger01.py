"""
Queremos optimizar el proceso que realiza un profesor en un aula de clases
para esto se debera realizar lo siguiente:
1.-Ingresar los apellidos de los alumnos y sus notas finales en un
diccionario dinamica hasta escribir la palabra fin
2.-Luegos mostar los siguiente datos:
2.1.-El apellido del alumno que tenga la nota mas alta inclusive mostrar la nota
2.2.-El apellido del alumno que tenga la nota mas baja inclusive mostrar la nota
2.3.-El Promedio General de la clase
"""
con =0
acum_notas=0
alumnos ={}

while True:
    apellido=input("Ingrese el apellido del alumno (o fin para terminar):")
    if apellido.lower() =='fin':
        break
    nota = float(input("Ingrese la Nota del alumno:"))
    alumnos[apellido]=nota
    con +=1 #Contador me indicar la cantidad de alumnos que estoy ingresando
    acum_notas +=nota #Acumulando las notas de la clase
    
alumno_mejor_nota=max(alumnos,key=alumnos.get) #clave = nombre
mejor_nota=alumnos[alumno_mejor_nota] #valor que es el apellido

alumno_menor_nota=min(alumnos,key=alumnos.get) #clave = nombre
menor_nota=alumnos[alumno_menor_nota] #valor que es el apellido

prom_clase= acum_notas / con

print(f"\nEl Alumno con mayor nota es {alumno_mejor_nota} con una nota de {mejor_nota} ")

print(f"\nEl Alumno con menor nota es {alumno_menor_nota} con una nota de {menor_nota} ")

print(f"\nEl Promedio de la clase es {round(prom_clase,2)}")









