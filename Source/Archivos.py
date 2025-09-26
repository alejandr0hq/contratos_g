import os
from .Estado import contratos_generados, contador_contratos
from .Registro import guardar_registro
from .Logger import logging
import Source.Estado as Estado

def guardar_archivo(contenido, tipo, datos):
    global contador_contratos
    try:
        directorio = 'contratos'
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        if tipo == 'prestacion_servicios':
            cliente = datos['nombre_completo_cliente']
        elif tipo == 'arrendamiento':
            cliente = datos['nombre_completo_arrendatario']
        else:
            cliente = datos['nombre_completo_comprador']

        cliente_formato = "".join(c for c in cliente if c.isalnum() or c in (' ', '_')).rstrip()
        cliente_formato = cliente_formato.replace(' ', '_')
        nombre_archivo = f"{directorio}/{tipo}_{cliente_formato}_{contador_contratos}.txt"
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)

        info_contrato = (contador_contratos, tipo, nombre_archivo, cliente, contenido)
        contratos_generados.append(info_contrato)
        guardar_registro(info_contrato)
        print("\n" + "=" * 55)
        print(f"\n- - - Archivo creado exitosamente: {nombre_archivo} - - -")
        print(f"- - - ID del contrato: {contador_contratos}. - - -\n")
        print("=" * 55)
        contador_contratos += 1
        Estado.contador_contratos = contador_contratos
        return nombre_archivo
    except Exception as error:
        error_msg = f"Error al crear el archivo: {error}"
        print(error_msg)
        logging.error(error_msg)
        return guardar_contrato_memoria(contenido, tipo, datos)

def guardar_contrato_memoria(contenido, tipo, datos):
    global contador_contratos
    try:
        if tipo == 'prestacion_servicios':
            cliente = datos['nombre_completo_cliente']
        elif tipo == 'arrendamiento':
            cliente = datos['nombre_completo_arrendatario']
        else:
            cliente = datos['nombre_completo_comprador']
        cliente_limpio = "".join(c for c in cliente if c.isalnum() or c in (' ', '_')).rstrip()
        nombre_archivo = f"{tipo}_{cliente_limpio.replace(' ', '_')}_{contador_contratos}.txt"
        info_contrato = (contador_contratos, tipo, nombre_archivo, cliente, contenido)
        contratos_generados.append(info_contrato)
        print("\n" + "=" * 55)
        print(f"\n- - - Contrato generado exitosamente con ID: {contador_contratos}. - - -")
        print("- - - (Guardado solo en memoria). - - -\n")
        contador_contratos += 1
        Estado.contador_contratos = contador_contratos
        return nombre_archivo
    except Exception as error:
        error_msg = f"Error al generar el contrato: {error}"
        print(error_msg)
        logging.error(error_msg)
        return None