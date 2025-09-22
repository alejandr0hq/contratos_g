# Importar funciones
from Menu import *
from Opción import *
from Salir import *
from Contrato_arrendamiento import *
from Datos import *

opcion = ""

def generar_contratos ( ) :
    print ( "\n" + "=" * 55 )
    print ( "\t\tGENERAR CONTRATOS" )
    print ( "=" * 55 )
    print ( "1. Contrato de Arrendamiento." )
    print ( "2. Contrato de Prestación de Servicios." )
    print ( "3. Contrato de Compra-Venta" )
    print ( "4. Volver." )
    print ( "=" * 55 )



# Programa
while opcion != "6" :
    menu ( )
    opcion = str ( opcion_menu ( ) )
    
    if opcion == "1" :
        generar_contratos ( )
        opcion = str ( opcion_menu ( ) )
        
        while opcion != "4" :

            if opcion == "1" :
                contrato_arrendamiento ( datos )

            elif opcion == "2" :
                #contrato_prestacion_servicios ( )
                continue

            elif opcion == "3" :
                #contrato_compraventa ( )
                continue

            elif opcion == "4" :
                break

            else:
                print ( "\n" + "=" * 55 )
                print ( "\n- - - Seleccione una opción válida. - - -\n" )
                print ( "=" * 55 )

    elif opcion == "2" :
        ver_contratos_generados ( )

    elif opcion == "3" :
        buscar_contrato ( )

    elif opcion == "4" :
        mostrar_contrato_completo ( )

    elif opcion == "5" :
        editar_contrato_existente ( )

    elif opcion == "6" :
        salir ( )

    else :
        print ( "\n" + "=" * 55 )
        print ( "\n - - - Seleccione una opción válida. - - -\n" )
        print ( "=" * 55 )