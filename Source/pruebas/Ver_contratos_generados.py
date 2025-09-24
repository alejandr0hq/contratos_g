def ver_contratos_generados ( ) :

    if not contratos_generados :
        print ( "\n" + "=" * 55 )
        print ( "\n- - - No hay contratos generados aún. - - -\n" )
        print ( "=" * 55 )
        return 
    
    print ( "\n" + "=" * 55 )
    print ( "\n- - - Contratos generados. - - -\n" )
    print ( "=" * 55 )
    print ( f"{'ID':<5} | {'Tipo de contrato':<30} | {'Cliente':<30} | {'Archivo':<50}")
    print ( "-" * 130 )

    for contrato in contratos_generados :
        id_contrato , tipo , archivo , cliente , contenido = contrato
        tipo_mostrar = tipo.replace ( '_' , ' ' ).title ( )

        print ( f"{str ( id_contrato ):<5} | {tipo_mostrar:<30} | {cliente:<30} | {archivo:<50}" )
        