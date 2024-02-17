"""
Prioridad operadores
====================
1.-Parentesis
()
2.-Exponente
**
3.-Negacion unaria (not)
-x,+x
4.-Multiplicacion,Division,Modulo
*,/,%
5.-Suma , Resta
+, -
6.-Concatenacion de Caracteres
+
"""
"""
Prioridad entre operadores aritmeticos
    resultado= 5 + 3 * 2 - 4 / 2
    #Solucion Primero se realiza la Mul (3*2=6) 
    #Segundo Luego la Division (4 / 2 =2) 
    #Tercer Suma (5+6 = 11)
    #Finalmente la resta (11 - 2 =9)
    print(resultado)
"""
"""
Prioridad de operadores Logicos
a= True
b= False
c= True
resultado = a and b or c
#Solucion : Primero se realiza la operacion 'and' , luego 'or'
#True and False = False , Luego False or True = True
print(resultado)
"""
"""
Prioridad de Operaciones de comparacion

x=10
y=5
z=8
resultado = x > y and x <=z
#Solucion :Primero se evalua x > y , y luego x <=z y finalmente and
#True and False = True
print(resultado)
"""

"""
Ejemplo de Negacion unaria (NOT)

contraseña_correcta = "secreto123"
contraseña_ingresada = input("Ingrese la Contraseña:")

if not contraseña_ingresada == contraseña_correcta:#True
    print("Contraseña Incorrecta,Acceso Denegado")
else:
    print("Contraseña Correcta,Acceso Permitido")
"""


"""
1.-Parantesis
2.-Exponente =16
3.-Multi = 16 * 3 = 48
4.-Division = 8 / 2 3 es 4
5.-Adicion = 2 + 48 = 50
6._Resta = 50 - 4 = 46
"""

resultado = 2 + 3 * 4 ** 2 - (8 / 2)
print(resultado)





















