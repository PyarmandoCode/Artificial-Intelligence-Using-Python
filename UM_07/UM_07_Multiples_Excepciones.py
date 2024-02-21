# def dividir_numero(a=None,b=None):
#     try:
#         resultado= a / b
#         print(f"Resultado {resultado}")
#     except ZeroDivisionError:
#         print("No se puede dividir entre cero")    
#     except TypeError:
#         print("Ambos Valores deben ser numericos")    
#     except Exception as e:    
#         print(f"error inesperado {e}")
#     else:
#         print("Se ejecuto el program de forma satisfactoria")    
#     finally:
#         print("todos los archivos se cerraron correctamente")    

# dividir_numero()

def mensaje_bienvenida(nom=None):
    print(f"Hola {nom} Que bueno tenerte por aca")

mensaje_bienvenida()    
