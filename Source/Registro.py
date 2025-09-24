def guardar_registro ( info_contrato ) :
    try :
        with open ( 'contratos_registro.txt' , 'a' , encoding = 'utf-8' ) as f :
            id_contrato , tipo , nombre_archivo , cliente , _ = info_contrato
            cliente_formato = cliente.replace('|', '_')
            linea = f"{id_contrato}|{tipo}|{nombre_archivo}|{cliente_formato}\n"
            f.write ( linea )
    except Exception as error :
        error_msg = f"Error al guardar el registro del contrato: {error}"
        print ( error_msg )
        logging.error ( error_msg )

def actualizar_registro ( ) :
    try :
        with open ( 'contratos_registro.txt' , 'w' , encoding = 'utf-8' ) as f :
            for info_contrato in contratos_generados :
                id_contrato , tipo , nombre_archivo , cliente , _ = info_contrato
                cliente_formato = cliente.replace('|', '_')
                linea = f"{id_contrato}|{tipo}|{nombre_archivo}|{cliente_formato}\n"
                f.write ( linea )
    except Exception as error :
        error_msg = f"Error al actualizar el archivo de registro: {error}"
        print ( error_msg )
        logging.error ( error_msg )

def cargar_contratos_desde_registro ( ) :
    global contratos_generados , contador_contratos
    print ( "\n" + "=" * 55 )
    print ( "\n- - - Buscando contratos guardados... - - -\n" )
    print ( "=" * 55 )
    max_id = 0
    contratos_cargados = 0
    contratos_con_errores = 0
    try :
        with open ( 'contratos_registro.txt' , 'r' , encoding = 'utf-8' ) as f :
            for numero_linea , linea in enumerate ( f , 1 ) :
                try :
                    partes = linea.strip ( ).split ( '|' )
                    if len ( partes ) == 4 :
                        id_contrato_str , tipo , archivo , cliente = partes
                        id_contrato = int ( id_contrato_str )
                        contenido = ""
                        if os.path.exists ( archivo ) :
                            try :
                                with open ( archivo , 'r' , encoding = 'utf-8' ) as contrato_file:
                                    contenido = contrato_file.read ( )
                            except Exception as error :
                                logging.error ( f"Error al leer archivo {archivo}: {error}" )
                                contenido = f"[Error al leer archivo: {error}]"
                        else :
                            contenido = "[Archivo no encontrado]"
                        info_contrato = ( id_contrato , tipo , archivo , cliente , contenido )
                        contratos_generados.append ( info_contrato )
                        contratos_cargados += 1
                        if id_contrato > max_id :
                            max_id = id_contrato
                    else :
                        contratos_con_errores += 1
                        logging.error ( f"Línea {numero_linea} del registro mal formateada: {linea}" )
                except Exception as error :
                    contratos_con_errores += 1
                    error_msg = f"Error al procesar línea {numero_linea} del registro: {error}"
                    logging.error ( error_msg )
        contador_contratos = max_id + 1
        if contratos_cargados > 0 :
            print ( "\n" + "=" * 55 )
            print ( f"\n- - - Se cargaron {contratos_cargados} contratos exitosamente. - - -\n" )
            print ( "=" * 55 )
        if contratos_con_errores > 0 :
            print ( "\n" + "=" * 55 )
            print ( f"\n- - - {contratos_con_errores} contratos tuvieron errores al cargar. - - -\n" )
            print ( "=" * 55 )
        if contratos_cargados == 0 and contratos_con_errores == 0 :
            print ( "\n" + "=" * 55 )
            print ( "\n- - - No se encontraron contratos guardados. - - -\n" )
            print ( "=" * 55 )
    except FileNotFoundError :
        print ( "\n" + "=" * 55 )
        print ( "\n- - - Archivo de registro no encontrado. Se creará uno nuevo al generar el primer contrato. - - -\n" )
        print ( "=" * 55 )
    except Exception as error :
        error_msg = f"Error al leer el archivo de registro: {error}"
        print ( error_msg )
        logging.error ( error_msg )