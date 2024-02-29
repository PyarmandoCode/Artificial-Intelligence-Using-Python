precios=[1200,1900,1700,1900,"Juan",True,[1200,90]]
precios[0] = 1900


precios.append("Python") #Metodo Añadir elementos a la lista al final
precios.insert(1,"Armando")#Metodo Añadir elementos en la posicion indicada
precios.pop(1)#Metodo eliminar elementos de la lista por su posicion
precios.remove("Juan")#Metodo eliminar elementos de la lista por su valor
nombres=["Juan","Pedro","Arturo","Beto"]
nombres.sort()
nombres.reverse()
nombres[2]="Armando" #metodo reemplazar elementos
cant=len(nombres)

lista=[1,2,3,4]
temp=lista[1]
lista[1]=lista[2]
lista[2]=temp

print(nombres)
print(cant)
