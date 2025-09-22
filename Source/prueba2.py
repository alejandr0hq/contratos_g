# CODIGO CORREGIDO PARA CREAR ARCHIVOS REALES Y EDITAR CONTRATOS
# SIN LIBRERIAS - SOLO FUNDAMENTOS DE PROGRAMACION

# Variables globales (mismas del codigo original)
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
    }
}

contratos_generados = []
contador_contratos = 1

# TODAS LAS FUNCIONES ORIGINALES (copiadas exactamente igual)
def obtener_fecha_actual():
    """Función para obtener fecha actual del usuario"""
    while True:
        try:
            fecha = input("Ingrese la fecha actual (DD/MM/AAAA): ")
            if validar_fecha(fecha):
                return fecha
            else:
                print("Formato de fecha inválido. Use DD/MM/AAAA")
        except:
            print("Error al ingresar la fecha. Intente nuevamente.")

def validar_fecha(fecha):
    """Valida formato básico de fecha DD/MM/AAAA"""
    if len(fecha) != 10:
        return False
    if fecha[2] != '/' or fecha[5] != '/':
        return False
    
    try:
        dia = int(fecha[0:2])
        mes = int(fecha[3:5])
        año = int(fecha[6:10])
        
        if dia < 1 or dia > 31:
            return False
        if mes < 1 or mes > 12:
            return False
        if año < 2020 or año > 2030:
            return False
        return True
    except:
        return False

def mostrar_menu_principal():
    """Muestra el menú principal del programa"""
    print("\n" + "="*55)
    print("    GENERADOR DE CONTRATOS - VERSION COMPLETA")
    print("="*55)
    print("1. Generar Contrato de Prestacion de Servicios")
    print("2. Generar Contrato de Arrendamiento")
    print("3. Ver contratos generados")
    print("4. Buscar contrato")
    print("5. Mostrar contrato completo")
    print("6. Editar contrato existente")
    print("7. Salir")
    print("="*55)

def validar_entrada(campo, valor):
    """Valida las entradas según el tipo de campo"""
    try:
        if 'cedula' in campo.lower():
            if not valor.isdigit():
                raise ValueError("La cédula debe contener solo números")
            if len(valor) < 6:
                raise ValueError("La cédula debe tener al menos 6 dígitos")
        
        elif 'valor' in campo.lower() or 'deposito' in campo.lower():
            numero = float(valor)
            if numero <= 0:
                raise ValueError("El valor debe ser mayor a 0")
        
        elif 'duracion' in campo.lower() and 'mes' in campo.lower():
            meses = int(valor)
            if meses <= 0 or meses > 120:
                raise ValueError("La duración debe ser entre 1 y 120 meses")
        
        elif 'fecha' in campo.lower():
            if not validar_fecha(valor):
                raise ValueError("Use formato DD/MM/AAAA")
        
        elif len(valor.strip()) == 0:
            raise ValueError("Este campo no puede estar vacío")
            
        return True
        
    except ValueError as e:
        print("Error de validación: " + str(e))
        return False

def solicitar_datos(tipo_contrato):
    """Solicita los datos necesarios para el contrato"""
    datos = {}
    plantilla = plantillas_contratos[tipo_contrato]
    
    print("\n--- DATOS PARA " + plantilla['titulo'] + " ---")
    
    for campo in plantilla['campos']:
        while True:
            try:
                campo_formateado = campo.replace('_', ' ').title()
                valor = input(campo_formateado + ": ").strip()
                
                if validar_entrada(campo, valor):
                    datos[campo] = valor
                    break
                    
            except:
                print("Error inesperado al procesar la entrada")
    
    return datos

def generar_contrato_prestacion(datos):
    """Genera el contenido del contrato de prestación de servicios"""
    fecha_actual = obtener_fecha_actual()
    
    contrato = """
""" + plantillas_contratos['prestacion_servicios']['titulo'] + """

Entre los suscritos a saber: """ + datos['nombre_prestador'] + """, identificado(a) con 
cédula de ciudadanía No. """ + datos['cedula_prestador'] + """, domiciliado(a) en 
""" + datos['direccion_prestador'] + """, quien en adelante se denominará EL PRESTADOR, 
y """ + datos['nombre_cliente'] + """, identificado(a) con cédula de ciudadanía 
No. """ + datos['cedula_cliente'] + """, domiciliado(a) en """ + datos['direccion_cliente'] + """, 
quien en adelante se denominará EL CLIENTE, hemos convenido celebrar el 
presente contrato de prestación de servicios.

CLÁUSULAS:

PRIMERA - OBJETO: El prestador se compromete a prestar los siguientes servicios:
""" + datos['descripcion_servicio'] + """

SEGUNDA - VALOR: El valor total del contrato es de $""" + datos['valor_contrato'] + """ 
pesos, que se pagará de la siguiente forma: """ + datos['forma_pago'] + """

TERCERA - DURACIÓN: El presente contrato tendrá vigencia desde el 
""" + datos['fecha_inicio'] + """ hasta el """ + datos['fecha_fin'] + """.

CUARTA - OBLIGACIONES: Las partes se comprometen a cumplir con las 
obligaciones establecidas en este contrato.

Dado en """ + datos['ciudad'] + """, a los """ + fecha_actual + """

_________________________          _________________________
EL PRESTADOR                        EL CLIENTE
""" + datos['nombre_prestador'] + """          """ + datos['nombre_cliente'] + """
C.C. """ + datos['cedula_prestador'] + """     C.C. """ + datos['cedula_cliente'] + """
"""
    return contrato

def generar_contrato_arrendamiento(datos):
    """Genera el contenido del contrato de arrendamiento"""
    fecha_actual = obtener_fecha_actual()
    
    contrato = """
""" + plantillas_contratos['arrendamiento']['titulo'] + """

Entre los suscritos a saber: """ + datos['nombre_arrendador'] + """, identificado(a) con 
cédula de ciudadanía No. """ + datos['cedula_arrendador'] + """, domiciliado(a) en 
""" + datos['direccion_arrendador'] + """, quien en adelante se denominará EL ARRENDADOR, 
y """ + datos['nombre_arrendatario'] + """, identificado(a) con cédula de ciudadanía 
No. """ + datos['cedula_arrendatario'] + """, domiciliado(a) en """ + datos['direccion_arrendatario'] + """, 
quien en adelante se denominará EL ARRENDATARIO, hemos convenido celebrar el 
presente contrato de arrendamiento.

CLÁUSULAS:

PRIMERA - OBJETO: El arrendador entrega en arrendamiento al arrendatario el 
inmueble ubicado en: """ + datos['direccion_inmueble'] + """

SEGUNDA - VALOR: El canon mensual de arrendamiento es de $""" + datos['valor_arriendo'] + """ 
pesos, que se pagará dentro de los primeros cinco (5) días de cada mes.

TERCERA - DEPÓSITO: El arrendatario entrega como depósito de garantía la suma de 
$""" + datos['valor_deposito'] + """ pesos.

CUARTA - DURACIÓN: El presente contrato tendrá una duración de """ + datos['duracion_meses'] + """ 
meses, contados a partir del """ + datos['fecha_inicio'] + """.

QUINTA - OBLIGACIONES: Las partes se comprometen a cumplir con las obligaciones 
establecidas por la ley y este contrato.

Dado en """ + datos['ciudad'] + """, a los """ + fecha_actual + """

_________________________          _________________________
EL ARRENDADOR                       EL ARRENDATARIO
""" + datos['nombre_arrendador'] + """         """ + datos['nombre_arrendatario'] + """
C.C. """ + datos['cedula_arrendador'] + """    C.C. """ + datos['cedula_arrendatario'] + """
"""
    return contrato

# FUNCION MEJORADA PARA GUARDAR ARCHIVOS REALES
def guardar_contrato_archivo_real(contenido, tipo, datos):
    """Guarda el contrato en un archivo de texto real"""
    global contador_contratos
    
    try:
        # Obtener nombre del cliente
        if tipo == 'prestacion_servicios':
            cliente = datos['nombre_cliente']
        else:
            cliente = datos['nombre_arrendatario']
        
        nombre_archivo = tipo + "_" + cliente.replace(' ', '_') + "_" + str(contador_contratos) + ".txt"
        
        # CREAR Y ESCRIBIR ARCHIVO REAL
        archivo = open(nombre_archivo, 'w', encoding='utf-8')
        archivo.write(contenido)
        archivo.close()
        
        # También guardar en memoria para consultas
        info_contrato = (contador_contratos, tipo, nombre_archivo, cliente, contenido)
        contratos_generados.append(info_contrato)
        
        print("\nArchivo creado exitosamente: " + nombre_archivo)
        print("ID del contrato: " + str(contador_contratos))
        
        contador_contratos = contador_contratos + 1
        return nombre_archivo
        
    except Exception as e:
        print("Error al crear el archivo: " + str(e))
        # Si falla, guardar solo en memoria
        return guardar_contrato_memoria(contenido, tipo, datos)

def guardar_contrato_memoria(contenido, tipo, datos):
    """Función de respaldo: guarda solo en memoria si no se puede crear archivo"""
    global contador_contratos
    
    try:
        if tipo == 'prestacion_servicios':
            cliente = datos['nombre_cliente']
        else:
            cliente = datos['nombre_arrendatario']
        
        nombre_archivo = tipo + "_" + cliente.replace(' ', '_') + "_" + str(contador_contratos) + ".txt"
        
        info_contrato = (contador_contratos, tipo, nombre_archivo, cliente, contenido)
        contratos_generados.append(info_contrato)
        
        print("\nContrato generado exitosamente con ID: " + str(contador_contratos))
        print("(Guardado solo en memoria)")
        
        contador_contratos = contador_contratos + 1
        return nombre_archivo
        
    except Exception as e:
        print("Error al generar el contrato: " + str(e))
        return None

def ver_contratos_generados():
    """Muestra la lista de contratos generados"""
    if len(contratos_generados) == 0:
        print("\nNo hay contratos generados aún.")
        return
    
    print("\n--- CONTRATOS GENERADOS ---")
    print("ID | Tipo                | Cliente              | Archivo")
    print("-" * 65)
    
    for contrato in contratos_generados:
        id_contrato, tipo, archivo, cliente, contenido = contrato
        tipo_mostrar = tipo.replace('_', ' ').title()
        cliente_corto = cliente[:18] + "..." if len(cliente) > 18 else cliente
        archivo_corto = archivo[:20] + "..." if len(archivo) > 20 else archivo
        
        print(str(id_contrato) + "  | " + tipo_mostrar.ljust(19) + " | " + 
              cliente_corto.ljust(20) + " | " + archivo_corto)

def buscar_contrato():
    """Permite buscar contratos por nombre de cliente"""
    if len(contratos_generados) == 0:
        print("\nNo hay contratos generados aún.")
        return
    
    termino_busqueda = input("\nIngrese el nombre del cliente a buscar: ").lower()
    contratos_encontrados = []
    
    for contrato in contratos_generados:
        id_contrato, tipo, archivo, cliente, contenido = contrato
        if termino_busqueda in cliente.lower():
            contratos_encontrados.append(contrato)
    
    if len(contratos_encontrados) > 0:
        print("\n--- CONTRATOS ENCONTRADOS (" + str(len(contratos_encontrados)) + ") ---")
        for contrato in contratos_encontrados:
            id_contrato, tipo, archivo, cliente, contenido = contrato
            print("ID: " + str(id_contrato))
            print("Tipo: " + tipo.replace('_', ' ').title())
            print("Cliente: " + cliente)
            print("Archivo: " + archivo)
            print("-" * 30)
    else:
        print("No se encontraron contratos con ese nombre de cliente.")

def mostrar_contrato_completo():
    """Muestra el contenido completo de un contrato"""
    if len(contratos_generados) == 0:
        print("\nNo hay contratos generados aún.")
        return
    
    try:
        id_buscar = int(input("\nIngrese el ID del contrato a mostrar: "))
        contrato_encontrado = None
        
        for contrato in contratos_generados:
            id_contrato, tipo, archivo, cliente, contenido = contrato
            if id_contrato == id_buscar:
                contrato_encontrado = contrato
                break
        
        if contrato_encontrado:
            id_contrato, tipo, archivo, cliente, contenido = contrato_encontrado
            print("\n" + "="*60)
            print("CONTRATO ID: " + str(id_contrato))
            print("ARCHIVO: " + archivo)
            print("="*60)
            print(contenido)
            print("="*60)
        else:
            print("No se encontró un contrato con ese ID.")
            
    except ValueError:
        print("Por favor ingrese un número válido.")
    except Exception as e:
        print("Error al buscar el contrato: " + str(e))

# NUEVA FUNCION PARA EDITAR CONTRATOS
def editar_contrato():
    """Permite editar un contrato existente"""
    if len(contratos_generados) == 0:
        print("\nNo hay contratos para editar.")
        return
    
    print("\n--- CONTRATOS DISPONIBLES PARA EDITAR ---")
    ver_contratos_generados()
    
    try:
        id_editar = int(input("\nIngrese el ID del contrato a editar: "))
        
        # Buscar el contrato
        contrato_encontrado = None
        indice_contrato = -1
        
        for i in range(len(contratos_generados)):
            id_actual, tipo, nombre_archivo, cliente, contenido = contratos_generados[i]
            if id_actual == id_editar:
                contrato_encontrado = contratos_generados[i]
                indice_contrato = i
                break
        
        if not contrato_encontrado:
            print("No se encontró el contrato con ID: " + str(id_editar))
            return
        
        id_actual, tipo, nombre_archivo, cliente, contenido_actual = contrato_encontrado
        
        print("\nEDITANDO CONTRATO ID: " + str(id_editar))
        print("Cliente actual: " + cliente)
        print("Tipo: " + tipo.replace('_', ' ').title())
        
        # Solicitar nuevos datos
        print("\n--- INGRESE LOS NUEVOS DATOS ---")
        nuevos_datos = solicitar_datos(tipo)
        
        if nuevos_datos:
            # Generar nuevo contenido
            if tipo == 'prestacion_servicios':
                nuevo_contenido = generar_contrato_prestacion(nuevos_datos)
            else:
                nuevo_contenido = generar_contrato_arrendamiento(nuevos_datos)
            
            # Intentar actualizar archivo
            try:
                archivo = open(nombre_archivo, 'w', encoding='utf-8')
                archivo.write(nuevo_contenido)
                archivo.close()
                print("Archivo actualizado: " + nombre_archivo)
            except:
                print("No se pudo actualizar el archivo, pero se actualizó en memoria.")
            
            # Actualizar en memoria
            nuevo_cliente = nuevos_datos.get('nombre_cliente', nuevos_datos.get('nombre_arrendatario', cliente))
            nueva_tupla = (id_actual, tipo, nombre_archivo, nuevo_cliente, nuevo_contenido)
            contratos_generados[indice_contrato] = nueva_tupla
            
            print("Contrato actualizado exitosamente!")
        else:
            print("Edición cancelada.")
            
    except ValueError:
        print("Por favor ingrese un número válido.")
    except Exception as e:
        print("Error al editar el contrato: " + str(e))

def programa_principal():
    """Función principal que ejecuta todo el programa"""
    print("Bienvenido al Generador de Contratos!")
    
    while True:
        try:
            mostrar_menu_principal()
            opcion = input("\nSeleccione una opción (1-7): ")
            
            if opcion == '1':
                datos = solicitar_datos('prestacion_servicios')
                if datos:
                    contenido = generar_contrato_prestacion(datos)
                    guardar_contrato_archivo_real(contenido, 'prestacion_servicios', datos)
            
            elif opcion == '2':
                datos = solicitar_datos('arrendamiento')
                if datos:
                    contenido = generar_contrato_arrendamiento(datos)
                    guardar_contrato_archivo_real(contenido, 'arrendamiento', datos)
            
            elif opcion == '3':
                ver_contratos_generados()
            
            elif opcion == '4':
                buscar_contrato()
            
            elif opcion == '5':
                mostrar_contrato_completo()
            
            elif opcion == '6':
                editar_contrato()
            
            elif opcion == '7':
                print("\nGracias por usar el Generador de Contratos!")
                break
            
            else:
                print("Opción inválida. Por favor seleccione una opción del 1 al 7.")
            
            input("\nPresione Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print("Error inesperado: " + str(e))
            print("Por favor, intente nuevamente.")

# Ejecutar el programa principal
programa_principal()