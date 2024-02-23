""" 
#todo Creacion de Entorno Virtual en VSC
#! Instalando la libreria para crear entornos
pip install virtualenv --user
#! Crear un directorio
mkdir paquetes_python
#! Ingresar al Directorio
cd .\paquetes_python\
#! Creando el Entorno Virtual
py -m venv .\paquetes_python\
#! Permisos
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
cd scripts
#! Activando el entorno Virtual
.\activate
"""