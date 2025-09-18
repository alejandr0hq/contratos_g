# Importar funciones
from Menu import *
from Opción import *
from Salir import *

# Título
def titulo ( ) :
    print("\n===========Generador de contratos legales=========== ")

opcion = ""

# Programa
while opcion != "4" :
    titulo ( )
    menu ( )
    opcion = str ( opcion_menu ( ) )
    if opcion == "1" :
        arrendamiento ( )
    elif opcion == "2" :
        prestacion_servicios ( )
    elif opcion == "3" :
        compra_venta ( )
    elif opcion == "4" :
        salir ( )