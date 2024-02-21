# try:
#     division = 20 /2 #cuerpo del bloque a evaluar
#     print(division)
# except Exception as err: #Cuando el bloque de codigo "try" encontrara un error
#     print("Ha Ocurrido un Error en el Codigo")
# else:
#     print("No Ha Ocurrido Ningun Error")  #Se ejecutara si no existiera una excepcion
# finally:
#     print("Se Cerraron todos los archivo correctamente") #Siempre se va a ejecutar exista o no error

#resultado= 10 * (1/0)
#print(resultado)#ZeroDivisionError: division by zero


#resultado = 4 + spam*3
#print (resultado) #name 'spam' is not defined

#resultado= '2' + 2
#print(resultado) #can only concatenate str (not "int") to str

#num1= int(input("Ingrese numero1:"))
#resultado=num1*20
#print(resultado) #ValueError: invalid literal for int() with base 10: 'A'

# lista = [1,2,3,4,5]
# try:
#     indice=int(input("Ingrese el indice:"))
#     elemento= lista[indice]
#     print(f"El Valor en el indice {elemento}")
# except IndexError:
#     print("No se encontro el indice en la lista o esta fuera de rango")   

try:
    numero=float(input("Ingrese un numero:")) 
    print(f"El Numero ingresado es {numero}")
except ValueError:
    print("Se esperaba un dato numerico")    
 
