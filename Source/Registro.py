def guardar_registro ( info_contrato ) :

    try :

        with open ( 'contratos_registro.txt' , "a" , encoding='utf-8' ) as f :
            id_contrato , tipo , nombre_archivo , cliente , _ = info_contrato
            linea = f"{id_contrato} | {tipo} | {nombre_archivo} | {cliente}\n"
            f.write ( linea )
    
    except Exception as e :
        print ( "\n" + "=" * 55 )
        print ( f"\n - - - Error: { e }. - - -\n" )
        print ( "=" * 55 )

def actualizar_registro ( ) :

    try :

        with open ( 'contratos_registro.txt' , "w" , encoding='utf-8' ) as f :

            for info_contrato in contratos_generados :
                id_contrato , tipo , nombre_archivo , cliente , _ = info_contrato
                linea = f"{id_contrato} | {tipo} | {nombre_archivo} | {cliente}\n"
                f.write ( linea )

    except Exception as e :
        print ( "\n" + "=" * 55 )
        print ( f"\n - - - Error: { e }. - - -\n" )
        print ( "=" * 55 )

def cargar_contratos_desde_registro ( ) :

    global contratos_generados, contador_contratos
    
    print("Buscando contratos guardados...")
    max_id = 0
    
    try:

        with open ( 'contratos_registro.txt' , 'r' , encoding='utf-8' ) as f :

            for linea in f:

                try:
                    partes = linea.strip().split('|')

                    if len(partes) == 4:
                        id_contrato_str , tipo , archivo , cliente = partes
                        id_contrato = int ( id_contrato_str )

                        with open ( archivo , 'r' , encoding='utf-8' ) as contrato_file :
                            contenido = contrato_file.read()                            
                        info_contrato = ( id_contrato , tipo , archivo , cliente , contenido )
                        contratos_generados.append ( info_contrato )

                        if id_contrato > max_id:
                            max_id = id_contrato
                    
                except Exception as e:
                    print ( "\n" + "=" * 55 )
                    print ( f"\n - - - Error: { e }. - - -\n" )
                    print ( "=" * 55 )
        
        contador_contratos = max_id + 1
        print ( "\n" + "=" * 55 )
        print ( f"\n- - - Se encontraron {len(contratos_generados)} contratos guardados. - - -\n" )
        print ( "=" * 55 )
        
    except FileNotFoundError :
        print ( "\n" + "=" * 55 )
        print ( "\n- - - Archivo de registro no encontrado. Se creará uno nuevo. - - -\n" )
        print ( "=" * 55)

    except Exception as e:
        print ( "\n" + "=" * 55 )
        print ( f"\n- - - Error: {e}. - - -\n" )
        print ( "=" * 55 )