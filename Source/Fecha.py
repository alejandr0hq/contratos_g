from Validar_datos import validar_fecha 

def fecha ( ) :
    while True :
        try :
            fecha = input ( "Ingrese la fecha actual (DD/MM/AAAA): " )
            if validar_fecha ( fecha ) :
                return fecha
            else :
                print ( "\n" + "=" * 55 )
                print ( "\n- - - Formato de fecha no válido. - - -\n" )
                print ( "=" * 55 )
        except :
            print ( "\n" + "=" * 55 )
            print ( "\n- - - Error al ingresar la fecha. - - -\n" )
            print ( "=" * 55 )