n1=float(input("Ingrese la Nota 1:"))
n2=float(input("Ingrese la Nota 2:"))
n3=float(input("Ingrese la Nota 3:"))
prom= (n1+n2+n2)/3
if prom>10.5:
    print("El Alumno Aprueba el curso")
else:
    sus=float(input("Ingrese la nota sustitutoria:"))
    nuepro=(sus+prom)/2
    if nuepro>10.5:
        print(f"El Alumno Aprobo el curso usando el sustitutorio round({nuepro},2)")
    else:
        print(f"El Alumno debera llevar nuevamente el curso round({nuepro},2)")    


