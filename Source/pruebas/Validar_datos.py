# Función que valida el formato de la fecha
def validar_fecha ( fecha ) :
    if len ( fecha ) != 10 :
        return False
    if fecha [ 2 ] != '/' or fecha [ 5 ] != '/' :
        return False
    try :
        dia = int ( fecha [ 0 : 2 ] )
        mes = int ( fecha [ 3 : 5 ] )
        año = int ( fecha [ 6 : 10 ] )
        if dia < 1 or dia > 31 :
            return False
        if mes <1 or mes > 12 :
            return False
        if año < 2025 or año > 2040 :
            return False
        return True
    except :
        return False 
    
# Función que valida el formato de los datos
def validar_datos ( campo , valor ) :
    try :
        if 'valor' in campo.lower ( ) or 'deposito' in campo.lower ( ) or 'bien' in campo.lower( ) :
            numero = float ( valor )
            if numero <= 0 :
                raise ValueError ( "El valor debe ser mayor a 0" )
            
        elif 'duracion' in campo.lower ( ) and 'mes' in campo.lower ( ) :
            meses = int ( valor )
            if meses <= 0 or meses > 120 :
                raise ValueError ( "\n- - - La duración debe ser entre 1 y 120 meses. - - -\n" )
        
        elif 'fecha' in campo.lower ( ) :
            if not validar_fecha ( valor ) :
                raise ValueError ( "\n- - - Use formato DD/MM/AAAA. - - -\n" )
        
        elif len ( valor.strip ( ) ) == 0 :
            raise ValueError ( "\n- - - Este campo no puede estar vacío. - - -\n" ) 
        
        return True
    
    except ValueError as e :
        print ( "\n" + "=" * 55 ) 
        print ( str ( e ) )
        print ( "=" * 55 )
        return False