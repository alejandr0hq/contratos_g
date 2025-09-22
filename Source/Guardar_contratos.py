from Programa import contratos_generados
 
# Función que guarda el contrato como archivo .txt
def guardar_contrato_archivo ( contenido , tipo , datos ) :
    global contador_contratos
    
    try:
        if tipo == 'prestacion_servicios' :
            cliente = datos [ 'nombre_cliente' ] 
        elif tipo == 'arrendamiento' : 
            cliente = datos [ 'nombre_arrendatario' ]
        else :
            cliente = datos [ 'nombre_comprador' ]

        nombre_archivo = f"c:{tipo}_{cliente.replace ( ' ' , '_' ) }_{str ( contador_contratos ) }.txt"

        with open ( nombre_archivo , "w" , encoding='utf-8' ) as archivo :
            archivo.write ( contenido )

        info_contrato = ( contador_contratos , tipo , nombre_archivo , cliente , contenido )
        contratos_generados.append ( info_contrato )
        guardar_registro ( info_contrato )

        print ( "\n" + "=" * 55 )
        print ( "\n- - - Archivo creado correctamente. - - -" )
        print ( f"- - - Guardado con el nombre {nombre_archivo} e ID {str ( contador_contratos ) }" )
        
        contador_contratos += 1
        return nombre_archivo
    
    except Exception as e :
        print ( "\n" + "=" * 55 )
        print ( f"\n- - - Error: { str ( e ) } - - -\n" )
        print ( "=" * 55 )

        # Si manda error lo guarda en la memoria
        return guardar_contrato_memoria ( contenido , tipo , datos )