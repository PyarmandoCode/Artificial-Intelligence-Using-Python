
"""
Tipo de Datos Primitivos

*Numericos
int
float

*Cadenas
str
'Este es un ejemplo de cadena'

*Booleanos
True/False

"""
edad = 28
nom_prod="Laptop" #str
prec_prod=1200.28 #float
estado=True
unidad=1

#print("Hola Mundo desde Python")
# print(type(edad))
# print(type(nom_prod))
# print(type(prec_prod))
# print(type(estado))

#prec_prod="1200.28"
#print(type(prec_prod))

"""
Conversion de Tipo de DATOS
CAST
1>str
2>int
3>float
4>bool
"""
dato= nom_prod + str(int(prec_prod))
#print(type(bool(unidad)))

precios=[] #Inicializar , Setear
precios=[1200,1900,1700,1900,"Juan",True,[1200,90]]
# print(precios[0]) #1200
# print(precios[4]) #"Juan"
# print(precios[6]) #[1200,90]
# print(precios[7]) #index rangen

#print(type(precios)) #List


"""
indentacion
bloques de codigo de espaciado 
"""
edad=20
if edad>=18:
    print("Es Mayor de edad")
else:
    print("Es Menor de edad")    









