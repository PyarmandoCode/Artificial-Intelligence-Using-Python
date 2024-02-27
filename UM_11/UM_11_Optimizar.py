"""
Realizar un programa que realize estas acciones:
-Ingresar 3 notas de un alumno
-Hallar su Promedio
-Si el alumno aprobo el curso
"""

# n1=int(input("Ingrese Nota 1:"))
# n2=int(input("Ingrese Nota 2:"))
# n3=int(input("Ingrese Nota 3:"))
# prom=(n1+n2+n3)/3
# if prom>10.5:
#     print("El Alumno Aprobo el curso")
# else:
#     print("El Alumno No Aprobo el curso")


# def calcular_promedio_final():
#     try:
#         lista_notas=list()
#         for nota in range(2):
#             notas_alumno=int(input("Ingrese la Nota {nota}"))
#             lista_notas.append(notas_alumno)
#         promedio = sum(lista_notas)/len(lista_notas)
#         respuesta=("Aprobo el curso" if promedio>= 10.5 else 'No Aprobo el curso')    
#         return respuesta
#     except ValueError as err:
#         print("Debe Ingresar los datos correctamente")    
#     else:
#         print("El codigo se ejecuto de manera correcta")    



#La Mayoria de Bucles que se pueden realizar dcon el for tambien podemos
#aplicarlo con el while

cont=1
while cont<=3:
    notas=int(input(f"Ingrese la Nota {cont}:"))
    cont +=1

for nota in range(1,4):
    notas=int(input(f"Ingrese la Nota {nota}:"))


notas =list()
while True:
    try:
        entrada=int(input(f"Ingrese una nota y \"fin\" para terminar :"))
        if entrada.lower=="fin":
            break
        nota=float(entrada)
        if 0 <= nota <=20:
            notas.append(nota)
        else:
            print("Ingrese una Nota Valida de 0 - 20")    
    except ValueError:    
            print("Ingrese un valor numerio correcto")    

        















