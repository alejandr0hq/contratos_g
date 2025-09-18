# Opción del menu
def opcion_menu ( ) :
    try :
        opcion = int ( input ( "Seleccione una opción del menu: " ) )
        return opcion 
    except ( ValueError , TypeError ) :
        print ( "-" * 178 )
        print ( "\n - - - Opción no válida. Ingrese una opción del 1 al 4. - - - \n" )
        print ( "-" * 178 )
        return opcion_menu ( )