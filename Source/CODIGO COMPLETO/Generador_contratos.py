# ====================================================================
# LIBRERÍAS
# ====================================================================

import os
from datetime import datetime
import logging

# ====================================================================
# LOGGING (ARCHIVO LOGS DE ERRORES) , DATETIME
# ====================================================================

logging.basicConfig (
    filename = 'contratos_errors.log' ,
    level = logging.ERROR ,
    format = '%(asctime)s - %(levelname)s - %(message)s' ,
    encoding = 'utf-8'
)

def fecha ( ) :
    ahora = datetime.now ( )
    return ahora.strftime ( "%Y/%m/%d  %H:%M:$S" )

# ====================================================================
# VARIABLES GLOBALES
# ====================================================================

from Plantillas import plantillas_contratos

contratos_generados = [ ]
contador_contratos = 1

# ====================================================================
# FUNCIONES DE VALIDACIÓN
# ====================================================================

def validar_nombre ( nombre ) :
    nombre = nombre.strip ( )
    if not nombre or len ( nombre.strip ( ) ) < 2 :
        return False
    return all ( c.isalpha ( ) or c.isspace ( ) for c in nombre)

def validar_telefono ( telefono ) :
    telefono = telefono.strip ( )
    return telefono.isdigit ( ) and 9 <= len ( telefono ) <= 13

def validar_precio ( precio_str ) :
    try :
        valor = float ( precio_str.replace ( ',' , '' ).replace ( '.' , '' ) )
        return valor > 0
    except ValueError :
        return False

def validar_entrada ( campo , valor ) :
    try:
        valor = valor.strip ( )        
        if not valor :
            raise ValueError ( "Este campo no puede estar vacío.")
        if 'nombre' in campo.lower ( ) :
            if not validar_nombre ( valor ) :
                raise ValueError ( "El nombre debe contener solo letras y espacios, mínimo 2 caracteres. " )
        elif 'telefono' in campo.lower():
            if not validar_telefono ( valor ) :
                raise ValueError ( "El teléfono debe tener entre 9 y 12 dígitos numéricos." )
        elif 'valor' in campo.lower ( ) or 'deposito' in campo.lower ( ) :
            if not validar_precio ( valor ) :
                raise ValueError ( "El valor debe ser un número mayor a 0.")
        elif 'duracion' in campo.lower ( ) and 'mes' in campo.lower ( ) :
            try:
                meses = int ( valor )
                if meses <= 0 or meses > 180 :
                    raise ValueError ( "La duración debe ser entre 1 y 180 meses." )
            except ValueError :
                raise ValueError ( "La duración debe ser un número entero." )
        elif 'fecha' in campo.lower ( ) :
            try :
                datetime.strptime ( valor , "%d/%m/%Y" )
            except ValueError :
                raise ValueError ( "La fecha debe tener el formato (DD/MM/AAAA)" )
        return True        
    except ValueError as error :
        print ( "\n" + "=" * 55 )
        print ( f"\n- - - Error de validación: {error}. - - -\n" )
        print ( "=" * 55 )
        return False

# ====================================================================
# MENUS
# ====================================================================

def mostrar_menu_principal ( ) :
    print ( "\n" + "=" * 55 )
    print ( "\t\tGENERADOR DE CONTRATOS" )
    print ( "=" * 55 )
    print ( "1. Generar Contrato." )
    print ( "2. Ver contratos generados." )
    print ( "3. Buscar contrato." )
    print ( "4. Mostrar contrato completo." )
    print ( "5. Editar contrato existente." )
    print ( "6. Borrar contrato." )
    print ( "7. Salir." )
    print ( "=" * 55 )

def mostrar_menu_contratos ( ) :
    print ( "\n" + "=" * 55 )
    print ( "\t\tGENERAR TIPO DE CONTRATO" )
    print ( "=" * 55 )
    print ( "1. Generar Contrato de Prestación de Servicios." )
    print ( "2. Generar Contrato de Arrendamiento." )
    print ( "3. Generar Contrato de Compra y Venta." )
    print ( "4. Volver." )
    print ( "=" * 55 )

# ====================================================================
# SOLICITAR DATOS
# ====================================================================

def solicitar_datos ( tipo_contrato ) :
    datos = { }
    plantilla = plantillas_contratos [ tipo_contrato ]
    print ( "\n" + "=" * 55 )
    print ( f"\n- - - DATOS PARA {plantilla['titulo']}. - - -\n" )
    print ( "=" * 55 )
    for campo in plantilla [ 'campos' ] :
        max_intentos = 5
        valor_valido = None
        for intento in range ( max_intentos ) :
            try :
                campo_formateado = campo.replace ( '_' , ' ' ).title ( )
                if 'fecha' in campo.lower ( ) :
                    prompt = f"{campo_formateado} (DD/MM/AAAA): "
                else :
                    prompt = f"{campo_formateado}: "
                valor = input ( prompt ).strip ( )
                if not any ( x in campo.lower ( ) for x in [ 'valor' , 'telefono' , 'fecha' , 'deposito' , 'duracion' , 'mes' ] ) :
                    valor = valor.title ( ) 
                if validar_entrada ( campo , valor ) :
                    valor_valido = valor
                    break
                else:
                    print ( "\n" + "=" * 55 )
                    print ( f"\n- - - Intento {intento + 1} de {max_intentos}. - - -\n" )
                    print ( "=" * 55 )
            except KeyboardInterrupt :
                print ( "\n" + "=" * 55 )
                print("\n- - - Operación cancelada por el usuario. - - -\n" )
                print ( "=" * 55 )
                return None
            except Exception as error :
                logging.error ( f"Error inesperado al procesar entrada para {campo}: {error}" )
                print ( "\n" + "=" * 55 )
                print ( "\n- - - Error inesperado al procesar la entrada. - - -\n" )
                print ( "=" * 55 )
        if valor_valido is None :
            print ( "\n" + "=" * 55 )
            print ( f"\n- - - Demasiados intentos fallidos para el campo {campo_formateado}. - - -\n" )
            print ( "=" * 55 )
            return None
        datos [ campo ] = valor_valido
    return datos

# ====================================================================
# REEMPLAZAR CONTENIDO CONTRATO
# ====================================================================

def reemplazar_contenido_contrato ( tipo_contrato , datos ) :
    fecha_actual = fecha ( ) 
    
    template_base = """
{titulo}

Entre los suscritos a saber: {parte1_nombre}, identificado(a) con 
teléfono celular No. {parte1_telefono}, domiciliado(a) en 
{parte1_direccion}, quien en adelante se denominará {parte1_rol}, 
y {parte2_nombre}, identificado(a) con teléfono celular 
No. {parte2_telefono}, domiciliado(a) en {parte2_direccion}, 
quien en adelante se denominará {parte2_rol}, hemos convenido 
celebrar el presente contrato.

CLÁUSULAS:

{clausulas}

Dado en {ciudad}, a los {fecha_actual}



_________________________          _________________________
{parte1_rol_mayuscula:<20} {parte2_rol_mayuscula:<20}
{parte1_nombre:<35} {parte2_nombre:<35}
Teléfono {parte1_telefono:<15} Teléfono {parte2_telefono:<15}
"""

    if tipo_contrato == 'prestacion_servicios':
        config = {
            'titulo': plantillas_contratos['prestacion_servicios']['titulo'],
            'parte1_nombre': datos['nombre_completo_prestador'],
            'parte1_telefono': datos['telefono_prestador'],
            'parte1_direccion': datos['direccion_prestador'],
            'parte1_rol': 'EL PRESTADOR',
            'parte1_rol_mayuscula': 'EL PRESTADOR',
            'parte2_nombre': datos['nombre_completo_cliente'],
            'parte2_telefono': datos['telefono_cliente'],
            'parte2_direccion': datos['direccion_cliente'],
            'parte2_rol': 'EL CLIENTE',
            'parte2_rol_mayuscula': 'EL CLIENTE',
            'ciudad': datos['ciudad'],
            'fecha_actual': fecha_actual,
            'clausulas': f"""PRIMERA - OBJETO: El prestador se compromete a prestar los siguientes servicios:
{datos['descripcion_servicio']}

SEGUNDA - VALOR: El valor total del contrato es de ${datos['valor_contrato']} 
pesos, que se pagará de la siguiente forma: {datos['forma_pago']}

TERCERA - DURACIÓN: El presente contrato tendrá vigencia desde el 
{datos['fecha_inicio']} hasta el {datos['fecha_fin']}.

CUARTA - OBLIGACIONES: Las partes se comprometen a cumplir con las 
obligaciones establecidas en este contrato."""
        }
    
    elif tipo_contrato == 'arrendamiento':
        config = {
            'titulo': plantillas_contratos['arrendamiento']['titulo'],
            'parte1_nombre': datos['nombre_completo_arrendador'],
            'parte1_telefono': datos['telefono_arrendador'],
            'parte1_direccion': datos['direccion_arrendador'],
            'parte1_rol': 'EL ARRENDADOR',
            'parte1_rol_mayuscula': 'EL ARRENDADOR',
            'parte2_nombre': datos['nombre_completo_arrendatario'],
            'parte2_telefono': datos['telefono_arrendatario'],
            'parte2_direccion': datos['direccion_arrendatario'],
            'parte2_rol': 'EL ARRENDATARIO',
            'parte2_rol_mayuscula': 'EL ARRENDATARIO',
            'ciudad': datos['ciudad'],
            'fecha_actual': fecha_actual,
            'clausulas': f"""PRIMERA - OBJETO: El arrendador entrega en arrendamiento al arrendatario el 
inmueble ubicado en: {datos['direccion_inmueble']}

SEGUNDA - VALOR: El canon mensual de arrendamiento es de ${datos['valor_arriendo']} 
pesos, que se pagará dentro de los primeros cinco (5) días de cada mes.

TERCERA - DEPÓSITO: El arrendatario entrega como depósito de garantía la suma de 
${datos['valor_deposito']} pesos.

CUARTA - DURACIÓN: El presente contrato tendrá una duración de {datos['duracion_meses']} 
meses, contados a partir del {datos['fecha_inicio']}.

QUINTA - OBLIGACIONES: Las partes se comprometen a cumplir con las obligaciones 
establecidas por la ley y este contrato."""
        }
    
    else:  
        config = {
            'titulo': plantillas_contratos['compra_venta']['titulo'],
            'parte1_nombre': datos['nombre_completo_vendedor'],
            'parte1_telefono': datos['telefono_vendedor'],
            'parte1_direccion': datos['direccion_vendedor'],
            'parte1_rol': 'EL VENDEDOR',
            'parte1_rol_mayuscula': 'EL VENDEDOR',
            'parte2_nombre': datos['nombre_completo_comprador'],
            'parte2_telefono': datos['telefono_comprador'],
            'parte2_direccion': datos['direccion_comprador'],
            'parte2_rol': 'EL COMPRADOR',
            'parte2_rol_mayuscula': 'EL COMPRADOR',
            'ciudad': datos['ciudad'],
            'fecha_actual': fecha_actual,
            'clausulas': f"""PRIMERA - OBJETO: El vendedor transfiere la propiedad del bien:
{datos['descripcion_bien']}

SEGUNDA - VALOR: El valor total de la transacción es de ${datos['valor_bien']}
pesos.

TERCERA - OBLIGACIONES: Las partes se comprometen a cumplir con las obligaciones
establecidas por la ley y este contrato.

CUARTA - FECHA: La presente transacción se realizó el {datos['fecha_transaccion']}."""
        }
    
    return template_base.format ( **config )
# ====================================================================
# GUARDAR CONTRATO
# ====================================================================

def guardar_archivo ( contenido , tipo , datos ) :
    global contador_contratos    
    try :
        directorio = 'contratos'
        if not os.path.exists ( directorio ) :
            os.makedirs ( directorio )
        if tipo == 'prestacion_servicios' :
            cliente = datos [ 'nombre_completo_cliente' ]
        elif tipo == 'arrendamiento' :
            cliente = datos [ 'nombre_completo_arrendatario' ]
        else :
            cliente = datos [ 'nombre_completo_comprador' ]

        cliente_formato = "".join(c for c in cliente if c.isalnum() or c in (' ', '_')).rstrip()
        cliente_formato = cliente_formato.replace(' ', '_')        
        nombre_archivo = f"{directorio}/{tipo}_{cliente_formato}_{contador_contratos}.txt"
        with open ( nombre_archivo , 'w' , encoding = 'utf-8' ) as archivo :
            archivo.write ( contenido )
        
        info_contrato = ( contador_contratos , tipo , nombre_archivo , cliente , contenido )
        contratos_generados.append ( info_contrato )
        guardar_registro ( info_contrato )
        print ( "\n" + "=" * 55 )
        print ( f"\n- - - Archivo creado exitosamente: {nombre_archivo} - - -" )
        print ( f"- - - ID del contrato: {contador_contratos}. - - -\n" )
        print ( "=" * 55 )
        contador_contratos += 1
        return nombre_archivo
    except Exception as error :
        error_msg = f"Error al crear el archivo: {error}"
        print ( error_msg )
        logging.error ( error_msg )
        return guardar_contrato_memoria ( contenido , tipo , datos )

def guardar_contrato_memoria ( contenido , tipo , datos ) :
    global contador_contratos    
    try:
        if tipo == 'prestacion_servicios' :
            cliente = datos [ 'nombre_completo_cliente' ]
        elif tipo == 'arrendamiento' :
            cliente = datos [ 'nombre_completo_arrendatario' ]
        else:
            cliente = datos [ 'nombre_completo_comprador' ]
        cliente_limpio = "".join ( c for c in cliente if c.isalnum ( ) or c in ( ' ' , '_' ) ).rstrip ( )
        nombre_archivo = f"{tipo}_{cliente_limpio.replace(' ', '_')}_{contador_contratos}.txt"
        info_contrato = ( contador_contratos , tipo , nombre_archivo , cliente, contenido )
        contratos_generados.append ( info_contrato )
        print ( "\n" + "=" * 55 )
        print ( f"\n- - - Contrato generado exitosamente con ID: {contador_contratos}. - - -" )
        print ( "- - - (Guardado solo en memoria). - - -\n" )
        contador_contratos += 1
        return nombre_archivo
    except Exception as error :
        error_msg = f"Error al generar el contrato: {error}"
        print ( error_msg )
        logging.error ( error_msg )
        return None

# ====================================================================
# VER CONTRATOS GENERADOS
# ====================================================================

def ver_contratos_generados ( ) :
    if not contratos_generados :
        print ( "\n" + "=" * 55 )
        print ( "\n- - - No hay contratos generados aún. - - -\n" )
        print ( "=" * 55 )
        return
    print ( "=" * 55 )
    print ("\n- - - CONTRATOS GENERADOS. - - -\n" )
    print ( "=" * 55 )
    print ( f"{'ID':<3} | {'Tipo':<25} | {'Cliente':<35} | {'Archivo':75} | {'Estado':<30}" )
    print ( "-" * 170)
    for contrato in contratos_generados :
        id_contrato , tipo, archivo , cliente , contenido = contrato
        tipo_mostrar = tipo.replace ( '_' , ' ' ).title ( )
        estado = "Archivo OK" if os.path.exists ( archivo ) else "Solo memoria"
        print ( f"{str(id_contrato):<3} | {tipo_mostrar:<25} | {cliente:<35} | {archivo:<75} | {estado:<30}")

# ====================================================================
# BUSCAR CONTRATOS
# ====================================================================

def buscar_contrato ( ) :
    if not contratos_generados :
        print ( "\n" + "=" * 55 )
        print ( "\n- - - No hay contratos generados aún. - - -\n" )
        print ( "=" * 55 )
        return
    print ( "\n" + "=" * 55 )
    print ( "\n- - - Buscar contratos. - - -\n" )
    print ( "=" * 55 )
    busqueda = input ("\nIngrese el nombre del cliente a buscar: " ).lower ( ).strip ( )
    if not busqueda:
        print ( "\n" + "=" * 55 )
        print ( "\n- - - Término de búsqueda vacío. - - -\n" )
        print ( "=" * 55 )
        return
    contratos_encontrados = [ ]
    for contrato in contratos_generados :
        id_contrato , tipo , archivo , cliente , contenido = contrato
        if busqueda in cliente.lower ( ) :
            contratos_encontrados.append ( contrato )
    if contratos_encontrados:
        print ( "\n" + "=" * 55 )
        print ( f"\n- - - CONTRATOS ENCONTRADOS ({len(contratos_encontrados)}). - - -\n" )
        for contrato in contratos_encontrados :
            id_contrato , tipo , archivo , cliente , contenido = contrato
            estado = "OK" if os.path.exists ( archivo ) else "Memoria"
            print ( f"{estado} ID: {id_contrato}" )
            print ( f"\tTipo: {tipo.replace ( '_' , ' ' ).title ( ) }" )
            print ( f"\tCliente: {cliente}" )
            print ( f"\tArchivo: {os.path.basename ( archivo ) }" )
            print ( "-" * 55)
        print ( "=" * 55 )
    else :
        print ( "\n" + "=" * 55 )
        print ( "\n- - - No se encontraron contratos con ese nombre de cliente. - - -\n" )
        print ( "=" * 55 )

# ====================================================================
# MOSTRAR CONTRATO (TERMINAL)
# ====================================================================

def mostrar_contrato_completo ( ) :
    if not contratos_generados :
        print ( "\n" + "=" * 55 )
        print ( "\n- - - No hay contratos generados aún. - - -\n" )
        print ( "=" * 55 )
        return
    try:
        id_buscar = int ( input ( "\nIngrese el ID del contrato a mostrar: " ) )
        contrato_encontrado = None
        for contrato in contratos_generados :
            id_contrato , tipo , archivo , cliente , contenido = contrato
            if id_contrato == id_buscar:
                contrato_encontrado = contrato
                break
        if contrato_encontrado :
            id_contrato , tipo , archivo , cliente , contenido = contrato_encontrado
            print ( "\n" + "=" * 55 )
            print ( f"\n- - - CONTRATO ID: {id_contrato}. - - -\n" )
            print ( f"\n- - - ARCHIVO: {os.path.basename(archivo)}. - - -\n" )
            if os.path.exists(archivo) :
                print ( "ESTADO: Archivo disponible" )
                try : 
                    with open ( archivo , 'r' , encoding = 'utf-8' ) as f :
                        contenido_archivo = f.read ( )
                    print ( "\n" + "=" * 55 )
                    print ( contenido_archivo )
                    print ( "\n" + "=" * 55 )
                except Exception as error :
                    print ( "\n" + "=" * 55 )
                    print ( f"- - - ESTADO: Error al leer archivo: {error}. - - -\n" )
                    print ( "\nMostrando contenido desde memoria:" )
                    print ( "=" * 55 )
                    print ( contenido )
                    print ( "=" * 55)
            else :
                print ( "\n" + "=" * 55 )
                print ( "\n- - - ESTADO: Archivo no encontrado, mostrando desde memoria. - - -\n" )
                print ( "=" * 55 )
                print ( contenido )
            print ( "=" * 55 )
        else :
            print ( "\n" + "=" * 55 )
            print ( "\n- - - No se encontró un contrato con ese ID. - - -\n" )
            print ( "=" * 55 )
    except ValueError :
        print ( "\n" + "=" * 55 )
        print ( "\n- - - Por favor ingrese un número válido. - - -\n" )
        print ( "=" * 55 )
    except Exception as error :
        error_msg = f"Error al buscar el contrato: {error}"
        print ( error_msg )
        logging.error ( error_msg )

# ====================================================================
# EDITAR CONTRATO
# ====================================================================

def editar_contrato ( ) :
    if not contratos_generados:
        print ( "\n" + "=" * 55 )
        print ( "\n- - - No hay contratos para editar. - - -\n" )
        print ( "=" * 55 )
        return
    print ( "\n" + "=" * 55 )
    print("\n- - - CONTRATOS DISPONIBLES PARA EDITAR - - -\n" )
    ver_contratos_generados ( )
    try:
        id_editar = int ( input ( "\nIngrese el ID del contrato a editar: " ) )
        contrato_encontrado = None
        indice_contrato = -1
        for i in range ( len ( contratos_generados ) ) :
            id_actual , tipo , nombre_archivo , cliente , contenido = contratos_generados [ i ]
            if id_actual == id_editar :
                contrato_encontrado = contratos_generados [ i ]
                indice_contrato = i
                break
        if not contrato_encontrado :
            print ( "\n" + "=" * 55 )
            print ( f"\n- - - No se encontró el contrato con ID: {id_editar}. - - - \n" )
            print ( "=" * 55 )
            return
        id_actual , tipo , nombre_archivo , cliente , contenido_actual = contrato_encontrado
        print ( "\n" + "=" * 55 )
        print ( f"\n- - - EDITANDO CONTRATO ID: {id_editar}. - - -" )
        print ( f"Cliente actual: {cliente}" )
        print ( f"Tipo: {tipo.replace('_', ' ').title()}" )
        confirmacion = input ("\n¿Desea continuar con la edición? (s/n): ").lower()
        if confirmacion != 'n' :
            print ( "\n" + "=" * 55 )
            print ( "Edición cancelada." )
            print ( "=" * 55 )
            return
        print("\n- - - INGRESE LOS NUEVOS DATOS. - - -\n")
        nuevos_datos = solicitar_datos(tipo)
        if nuevos_datos:
            nuevo_contenido = reemplazar_contenido_contrato ( tipo , nuevos_datos )            
            archivo_actualizado = False
            try:
                with open ( nombre_archivo , 'w' , encoding = 'utf-8' ) as archivo :
                    archivo.write ( nuevo_contenido )
                print ( "\n" + "=" * 55 )
                print ( f"\n- - - Archivo actualizado: {os.path.basename(nombre_archivo)}. - - -\n" )
                print ( "=" * 55 )
                archivo_actualizado = True
            except Exception as error:
                error_msg = f"No se pudo actualizar el archivo: {error}"
                print ( error_msg )
                logging.error ( error_msg )
                print ( "Los cambios se guardarán solo en memoria." )
            nuevo_cliente = nuevos_datos.get ( 'nombre_completo_cliente', 
                          nuevos_datos.get ( 'nombre_completo_arrendatario' , 
                          nuevos_datos.get ( 'nombre_completo_comprador' , cliente ) ) )
            nueva_tupla = (id_actual , tipo , nombre_archivo , nuevo_cliente , nuevo_contenido )
            contratos_generados [ indice_contrato ] = nueva_tupla
            try :
                actualizar_registro ( )
                print ( "\n" + "=" * 55 )
                print ( "\n- - - Registro actualizado correctamente. - - -\n" )
                print ( "=" * 55 )
            except Exception as error :
                error_msg = f"Error al actualizar registro: {error}"
                print ( error_msg )
                logging.error ( error_msg )
            print ( "\n" + "=" * 55 )
            print ( "\n- - - Contrato editado exitosamente. - - -\n" )
            print ( "=" * 55 )
        else :
            print ( "\n" + "=" * 55 )
            print ( "\n- - - Edición cancelada debido a errores en los datos. - - -\n" )
            print ( "=" * 55 )
    except ValueError :
        print ( "\n" + "=" * 55 )
        print ( "\n- - - Por favor ingrese un número válido. - - -\n" )
        print ( "=" * 55 )
    except Exception as error :
        error_msg = f"Error al editar el contrato: {error}"
        print ( error_msg )
        logging.error ( error_msg )
# ====================================================================
# BORRAR CONTRATO   
# ====================================================================
def borrar_contrato():
    print ( "\n" + "=" * 55 )
    print ( "\n- - - Borrar contratos. - - -\n" )
    print ( "=" * 55 )
    if not contratos_generados:
        print("\n" + "=" * 55)
        print("\n- - - No hay contratos para borrar. - - -\n")
        print("=" * 55)
        return
    try:
        id_borrar = int(input("\nIngrese el ID del contrato a borrar: "))
        contrato_encontrado = None
        indice_contrato = -1
        for i, contrato in enumerate(contratos_generados):
            id_actual, tipo, nombre_archivo, cliente, contenido = contrato
            if id_actual == id_borrar:
                contrato_encontrado = contrato
                indice_contrato = i
                break
        if contrato_encontrado:
            id_actual, tipo, nombre_archivo, cliente, contenido = contrato_encontrado
            confirmacion = input(f"\n¿Está seguro que desea borrar el contrato ID {id_actual}? (s/n): ").lower()
            if confirmacion == 's':
                if os.path.exists(nombre_archivo):
                    try:
                        os.remove(nombre_archivo)
                        print(f"\n- - - Archivo {os.path.basename(nombre_archivo)} eliminado. - - -")
                    except Exception as error:
                        print(f"\n- - - Error al eliminar el archivo: {error}. - - -")
                        logging.error(f"Error al eliminar archivo {nombre_archivo}: {error}")
                contratos_generados.pop(indice_contrato)
                actualizar_registro()
                print("\n" + "=" * 55)
                print(f"\n- - - Contrato ID {id_actual} borrado correctamente. - - -\n")
                print("=" * 55)
            else:
                print ( "\n" + "=" * 55 )
                print("\n- - - Operación cancelada. - - -\n")
                print ( "=" * 55 )
        else:
            print("\n" + "=" * 55)
            print("\n- - - No se encontró un contrato con ese ID. - - -\n")
            print("=" * 55)
    except ValueError:
        print("\n" + "=" * 55)
        print("\n- - - Por favor ingrese un número válido. - - -\n")
        print("=" * 55)
    except Exception as error:
        error_msg = f"Error al borrar el contrato: {error}"
        print(error_msg)
        logging.error(error_msg)

# ====================================================================
# REGISTRO   
# ====================================================================

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

# ====================================================================
# PROCESAMIENTO DE CONTRATOS
# ====================================================================

def procesar_generacion_contrato ( tipo_contrato ) :
    try :
        print ( "\n" + "=" * 55 )
        print ( f"\n- - - Iniciando generación de {tipo_contrato.replace ( '_' , ' ' ).title ( ) }. - - - \n" )
        print ( "=" * 55 )        
        datos = solicitar_datos ( tipo_contrato )
        if not datos :
            print ( "\n" + "=" * 55 )
            print ( "\n- - - Generación cancelada debido a errores en los datos. - - -\n" )
            print ( "=" * 55 )
            return False
        print ( "\n" + "=" * 55 )
        print ( "\n- - - Generando contrato... - - -\n" )
        print ( "=" * 55 )
        contenido = reemplazar_contenido_contrato ( tipo_contrato , datos )
        if contenido :
            print ( "\n" + "=" * 55 )
            print ( "\n- - - Guardando contrato... - - -\n" )
            print ( "=" * 55 )
            archivo_creado = guardar_archivo ( contenido , tipo_contrato , datos )
            if archivo_creado :
                print ( "\n" + "=" * 55 )
                print ( "\n- - - Contrato generado y guardado exitosamente - - -\n" )
                print ( "=" * 55 )
                return True
            else :
                print ( "\n" + "=" * 55 )
                print ( "\n- - - Error al guardar el contrato. - - -\n" )
                print ( "=" * 55 )
                return False
        else :
            print ( "\n" + "=" * 55 )
            print ( "\n- - - Error al generar el contenido del contrato. - - -\n" )
            print ( "=" * 55 )
            return False
    except Exception as error :
        error_msg = f"Error en el proceso de generación: {error}"
        print ( f"Error: {error_msg}" )
        logging.error ( error_msg )
        return False

# ====================================================================
# PROGRAMA PRINCIPAL
# ====================================================================

def programa_principal ( ) :
    print ( "\n" + "=" * 55 )
    print ( "\n- - - Bienvenido al Generador de Contratos - Versión 1.0 - - -" )
    print ( "- - - Sistema de gestión de contratos legales. - - -\n" )
    print ( "=" * 55 )
    cargar_contratos_desde_registro ( )
    while True:
        try:
            mostrar_menu_principal ( )
            opcion = input ( "\nSeleccione una opción (1-7): " ).strip ( )
            if opcion == '1':
                mostrar_menu_contratos ( )
                opcion = input ( "\nSeleccione una opción (1-4): " ).strip ( )
                if opcion == '1' :
                    procesar_generacion_contrato ( 'prestacion_servicios' )
                elif opcion == '2' :
                    procesar_generacion_contrato ( 'arrendamiento' )
                elif opcion == '3' :
                    procesar_generacion_contrato ( 'compra_venta' )
                elif opcion == '4' :
                    continue
                else :
                    print ( "\n" + "=" * 55 )
                    print ( "\n- - - Opción inválida. Por favor seleccione una opción del 1 al 4. - - -\n" )
                    print ( "=" * 55 )
            elif opcion == '2' :
                ver_contratos_generados( )
            elif opcion == '3' :
                buscar_contrato ( )
            elif opcion == '4' :
                mostrar_contrato_completo ( )
            elif opcion == '5' :
                editar_contrato ( )
            elif opcion == '6':
                borrar_contrato ( )
            elif opcion == '7' :
                print ( "\n" + "=" * 55 )
                print ( "\n- - - Gracias por usar el Generador de Contratos - - -")
                print ( "- - - Todos los contratos han sido guardados correctamente. - - -\n" )
                print ( "=" * 55 )
                break
            else:
                print ( "\n" + "=" * 55 )
                print ( "\n- - - Opción inválida. Por favor seleccione una opción del 1 al 7. - - -\n")
                print ( "=" * 55 )
            input("\nPresione Enter para continuar...")
        except KeyboardInterrupt :
            print ( "\n" + "=" * 55 )
            print ( "\n- - - Programa interrumpido por el usuario. - - -\n" )
            print ( "=" * 55 )
            confirmacion = input ( "¿Desea salir? (s/n): " ).lower ( )
            if confirmacion == 's' :
                break
        except Exception as error :
            error_msg = f"Error inesperado en el programa principal: {error}"
            print ( "\n" + "=" * 55 )
            print ( f"\n- - - Error: {error_msg}. - - -\n" )
            print ( "=" * 55 )
            logging.error ( error_msg )
            print ( "\n" + "=" * 55 )
            print ( "\n- - - Intentando continuar... - - -\n" )
            print ( "=" * 55 )

# ====================================================================
# PUNTO DE ENTRADA
# ====================================================================

if __name__ == "__main__":
    try:
        programa_principal()
    except Exception as error :
        error_msg = f"Error crítico al iniciar el programa: {error}"
        print ( "\n" + "=" * 55 )
        print ( f"Error: {error_msg}" )
        print ( "=" * 55 )
        logging.critical ( error_msg )
        input ( "Presione Enter para salir..." )