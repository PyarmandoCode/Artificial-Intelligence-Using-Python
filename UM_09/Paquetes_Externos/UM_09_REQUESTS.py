"""
Crear Un programa que se SOLICITE  un servicio externo (API) donde
se muestre los datos de un producto
1>Instalar la modulo requests que se encarga de hacer la peticion o conexion
al api
pip install requests
**********************
API ? "Interfaz de programacion de Aplicaciones"
Un Intermediario que permite que un programa obtenga acceso a funciones
especificas o datos de otra aplicacion.
"""
import requests
def obtener_datos_api(url):
    try:
        #Realizar la solicitud a la API
        respuesta=requests.get(url)
        #Verificar si la solicitud fue exitosa (codigo 200)
        if respuesta.status_code==200:
            #Cast los datos JSON y devolverlos como un diccionario
            datos_diccionario=respuesta.json()
            return datos_diccionario
        else:
            print(f"Error en la solicitud codigo estado {respuesta.status_code}")
            return None
    except Exception as e:
        print(f"Error en la solicitud {str(e)}")    
        return None

url_api_ejemplo="https://jsonplaceholder.typicode.com/todos/1"        
datos_api=obtener_datos_api(url_api_ejemplo)
if datos_api:
    print(datos_api)


        






