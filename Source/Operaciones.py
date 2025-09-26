
import os
from .Estado import contratos_generados
from .Logger import logging
from .Datos import solicitar_datos
from .Generador import reemplazar_contenido_contrato
from .Archivos import guardar_archivo
from .Registro import actualizar_registro

def ver_contratos_generados():
    if not contratos_generados:
        print("\n" + "=" * 55)
        print("\n- - - No hay contratos generados aún. - - -\n")
        print("=" * 55)
        return 
    print("\n" + "=" * 55)
    print("\n- - - Contratos generados. - - -\n")
    print("=" * 55)
    print(f"{'ID':<5} | {'Tipo de contrato':<30} | {'Cliente':<30} | {'Archivo':<50}")
    print("-" * 130)
    for contrato in contratos_generados:
        id_contrato, tipo, archivo, cliente, contenido = contrato
        tipo_mostrar = tipo.replace('_',' ').title()
        print(f"{str(id_contrato):<5} | {tipo_mostrar:<30} | {cliente:<30} | {archivo:<50}")

def buscar_contrato():
    if not contratos_generados:
        print("\n" + "=" * 55)
        print("\n- - - No hay contratos generados aún. - - -\n")
        print("=" * 55)
        return
    print("\n" + "=" * 55)
    print("\n- - - Buscar contratos. - - -\n")
    print("=" * 55)
    busqueda = input("\nIngrese el nombre del cliente a buscar: ").lower().strip()
    if not busqueda:
        print("\n" + "=" * 55)
        print("\n- - - Término de búsqueda vacío. - - -\n")
        print("=" * 55)
        return
    contratos_encontrados = []
    for contrato in contratos_generados:
        id_contrato, tipo, archivo, cliente, contenido = contrato
        if busqueda in cliente.lower():
            contratos_encontrados.append(contrato)
    if contratos_encontrados:
        print("\n" + "=" * 55)
        print(f"\n- - - CONTRATOS ENCONTRADOS ({len(contratos_encontrados)}). - - -\n")
        for contrato in contratos_encontrados:
            id_contrato, tipo, archivo, cliente, contenido = contrato
            estado = "OK" if os.path.exists(archivo) else "Memoria"
            print(f"{estado} ID: {id_contrato}")
            print(f"\tTipo: {tipo.replace('_', ' ').title()}")
            print(f"\tCliente: {cliente}")
            print(f"\tArchivo: {os.path.basename(archivo)}")
            print("-" * 55)
        print("=" * 55)
    else:
        print("\n" + "=" * 55)
        print("\n- - - No se encontraron contratos con ese nombre de cliente. - - -\n")
        print("=" * 55)

def mostrar_contrato_completo():
    if not contratos_generados:
        print("\n" + "=" * 55)
        print("\n- - - No hay contratos generados aún. - - -\n")
        print("=" * 55)
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
            print("\n" + "=" * 55)
            print(f"\n- - - CONTRATO ID: {id_contrato}. - - -\n")
            print(f"\n- - - ARCHIVO: {os.path.basename(archivo)}. - - -\n")
            if os.path.exists(archivo):
                print("ESTADO: Archivo disponible")
                try: 
                    with open(archivo, 'r', encoding='utf-8') as f:
                        contenido_archivo = f.read()
                    print("\n" + "=" * 55)
                    print(contenido_archivo)
                    print("\n" + "=" * 55)
                except Exception as error:
                    print("\n" + "=" * 55)
                    print(f"- - - ESTADO: Error al leer archivo: {error}. - - -\n")
                    print("\nMostrando contenido desde memoria:")
                    print("=" * 55)
                    print(contenido)
                    print("=" * 55)
            else:
                print("\n" + "=" * 55)
                print("\n- - - ESTADO: Archivo no encontrado, mostrando desde memoria. - - -\n")
                print("=" * 55)
                print(contenido)
            print("=" * 55)
        else:
            print("\n" + "=" * 55)
            print("\n- - - No se encontró un contrato con ese ID. - - -\n")
            print("=" * 55)
    except ValueError:
        print("\n" + "=" * 55)
        print("\n- - - Por favor ingrese un número válido. - - -\n")
        print("=" * 55)
    except Exception as error:
        error_msg = f"Error al buscar el contrato: {error}"
        print(error_msg)
        logging.error(error_msg)

def editar_contrato():
    if not contratos_generados:
        print("\n" + "=" * 55)
        print("\n- - - No hay contratos para editar. - - -\n")
        print("=" * 55)
        return
    print("\n" + "=" * 55)
    print("\n- - - CONTRATOS DISPONIBLES PARA EDITAR - - -\n")
    ver_contratos_generados()
    try:
        id_editar = int(input("\nIngrese el ID del contrato a editar: "))
        contrato_encontrado = None
        indice_contrato = -1
        for i in range(len(contratos_generados)):
            id_actual, tipo, nombre_archivo, cliente, contenido = contratos_generados[i]
            if id_actual == id_editar:
                contrato_encontrado = contratos_generados[i]
                indice_contrato = i
                break
        if not contrato_encontrado:
            print("\n" + "=" * 55)
            print(f"\n- - - No se encontró el contrato con ID: {id_editar}. - - - \n")
            print("=" * 55)
            return
        id_actual, tipo, nombre_archivo, cliente, contenido_actual = contrato_encontrado
        print("\n" + "=" * 55)
        print(f"\n- - - EDITANDO CONTRATO ID: {id_editar}. - - -")
        print(f"Cliente actual: {cliente}")
        print(f"Tipo: {tipo.replace('_', ' ').title()}")
        confirmacion = input("\n¿Desea continuar con la edición? (s/n): ").lower()
        if confirmacion != 'n':
            print("\n" + "=" * 55)
            print("Edición cancelada.")
            print("=" * 55)
            return
        print("\n- - - INGRESE LOS NUEVOS DATOS. - - -\n")
        nuevos_datos = solicitar_datos(tipo)
        if nuevos_datos:
            nuevo_contenido = reemplazar_contenido_contrato(tipo, nuevos_datos)
            archivo_actualizado = False
            try:
                with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                    archivo.write(nuevo_contenido)
                print("\n" + "=" * 55)
                print(f"\n- - - Archivo actualizado: {os.path.basename(nombre_archivo)}. - - -\n")
                print("=" * 55)
                archivo_actualizado = True
            except Exception as error:
                error_msg = f"No se pudo actualizar el archivo: {error}"
                print(error_msg)
                logging.error(error_msg)
                print("Los cambios se guardarán solo en memoria.")
            nuevo_cliente = nuevos_datos.get('nombre_completo_cliente',
                          nuevos_datos.get('nombre_completo_arrendatario',
                          nuevos_datos.get('nombre_completo_comprador', cliente)))
            nueva_tupla = (id_actual, tipo, nombre_archivo, nuevo_cliente, nuevo_contenido)
            contratos_generados[indice_contrato] = nueva_tupla
            try:
                actualizar_registro()
                print("\n" + "=" * 55)
                print("\n- - - Registro actualizado correctamente. - - -\n")
                print("=" * 55)
            except Exception as error:
                error_msg = f"Error al actualizar registro: {error}"
                print(error_msg)
                logging.error(error_msg)
            print("\n" + "=" * 55)
            print("\n- - - Contrato editado exitosamente. - - -\n")
            print("=" * 55)
        else:
            print("\n" + "=" * 55)
            print("\n- - - Edición cancelada debido a errores en los datos. - - -\n")
            print("=" * 55)
    except ValueError:
        print("\n" + "=" * 55)
        print("\n- - - Por favor ingrese un número válido. - - -\n")
        print("=" * 55)
    except Exception as error:
        error_msg = f"Error al editar el contrato: {error}"
        print(error_msg)
        logging.error(error_msg)
