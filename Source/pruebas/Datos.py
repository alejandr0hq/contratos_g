# Plantillas de los tipos de contratos
plantillas_contratos = {
    'prestacion_servicios': {
        'titulo': 'CONTRATO DE PRESTACIÓN DE SERVICIOS',
        'campos': [
            'nombre_prestador', 'cedula_prestador', 'direccion_prestador',
            'nombre_cliente', 'cedula_cliente', 'direccion_cliente',
            'descripcion_servicio', 'valor_contrato', 'fecha_inicio',
            'fecha_fin', 'forma_pago', 'ciudad'
        ]
    },
    'arrendamiento': {
        'titulo': 'CONTRATO DE ARRENDAMIENTO',
        'campos': [
            'nombre_arrendador', 'cedula_arrendador', 'direccion_arrendador',
            'nombre_arrendatario', 'cedula_arrendatario', 'direccion_arrendatario',
            'direccion_inmueble', 'valor_arriendo', 'valor_deposito',
            'fecha_inicio', 'duracion_meses', 'ciudad'
        ]
    },
    'compra_venta': {
        'titulo': 'CONTRATO DE COMPRA Y VENTA',
        'campos': [
            'nombre_vendedor', 'cedula_vendedor', 'direccion_vendedor',
            'nombre_comprador', 'cedula_comprador', 'direccion_comprador',
            'descripcion_bien', 'valor_bien', 'ciudad', 'fecha_transaccion'
        ]
    }
}

# Importar de otros archivos
from Validar_datos import validar_datos

# Función para solicitar los datos 
def datos ( tipo_contrato ) :
    datos = { }
    plantilla = plantillas_contratos [ tipo_contrato ]
    
    print ( "\n" + "=" * 55 )
    print ( "\n- - - Datos para " + plantilla [ 'titulo' ] + " - - -\n" )
    print ( "=" * 55 ) 

    for campo in plantilla [ 'campos' ] :

        while True :

            try :
                campo_formato = campo.replace ( '_' , ' ' ).title ( )
                
                if 'fecha' in campo.lower ( ) :
                    prompt = f"{campo_formato} (DD/MM/AAAA): "
                else :
                    prompt = f"{campo_formato}: "
                
                valor = input ( prompt ).strip ( )
                
                if validar_datos ( campo , valor ) :
                    datos [ campo ] = valor 
                    break
            
            except :
                print ( "\n" + "=" * 55 )
                print ( "\n- - - Error. - - -\n" )
                print ( "=" * 55 )
    
    return datos