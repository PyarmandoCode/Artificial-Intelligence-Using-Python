def mensaje(nom):
    #contenido de la funcion
    frase=f"Bienvenido {nom} al Curso de Python con IA "
    return frase

#print(mensaje("Armando"))
valores = [20,12,34,12,45,18]

global suma

def max_min_sum_pro(datos):
    maximo=max(datos)
    minimo=min(datos)
    suma=sum(datos)
    prom=suma/6
    valores = f"El Valor Maximo de la Lista es {maximo},El Valor Minimo de la Lista es {minimo} , La suma de los valores es {suma} y el promedio es {prom}"
    return valores

#print(max_min_sum_pro(valores))


# lista_numeros=[1,2,3,4,5]
# print(f"Lista Original {lista_numeros}")
# #Invertir la Lista
# lista_numeros.reverse()
# print(f"Lista Invertida {lista_numeros}")

"""
Funciones recursivas
Es Una funcion que se llame a si misma dentro de su propia definicion


def suma_naturales(n):
    #Caso base: suma de los primeros 0 numeros es 0
    if n == 0:
        return 0
    else:
        #Llamar recursiva: suma los primero n numeros 
        return n + suma_naturales (n - 1 )
    
    
n= 5
resultado = suma_naturales(n)
print(f"La Suma de los primeros {n} numeros naturales es  {resultado}")
"""

"""
funcion lambda .-son funciones pequeñas que generalmente se definen en una linea

def cuadrado(num):
    resultado = num **2
    return resultado

cuadrado = lambda x:x**2

numero = 4
resultado=cuadrado(numero)
print(f"El Cuadrado de {numero} es {resultado}")
"""

"""
def sumar(n1,n2):
    resultado= n1+n2
    return resultado
#print(sumar(12,18))

suma_lam= lambda n1,n2:n1+n2

resultado=suma_lam(12,18)
print(resultado)
"""

# def par_impar(num):
#     if num % 2 ==0:
#         resultado=f"el numero {num} es par"
#     else:
#         resultado=f"el numero {num} es impar"    
#     return resultado

# print(par_impar(11)) 

resultado=lambda num:num % 2==0
#print(resultado(4))#True
#print(resultado(7))#False


mayusculas = lambda s:s.upper()
resultado= mayusculas("python")
print(resultado)


