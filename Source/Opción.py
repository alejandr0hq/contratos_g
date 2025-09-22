# Función que pide la opción del menu
def opcion_menu ( ) :
    try :
        opcion = int ( input ( "\nSeleccione una opción del menu: " ) )
        return opcion 
    except ( ValueError , TypeError ) :
        print ( "\n" + "=" * 55 )
        print ( "\n - - - Opción no válida. Ingrese una opción del 1 al 4. - - - \n" )
        print ( "=" * 55 )
        return opcion_menu ( )