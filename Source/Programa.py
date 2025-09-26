from .Menus import mostrar_menu_principal, mostrar_menu_contratos
from .Datos import solicitar_datos
from .Generador import reemplazar_contenido_contrato
from .Archivos import guardar_archivo
from .Operaciones import (
    ver_contratos_generados,
    buscar_contrato,
    mostrar_contrato_completo,
    editar_contrato,
)
from .Registro import cargar_contratos_desde_registro
from .Logger import logging

def procesar_generacion_contrato(tipo_contrato):
    try:
        print("\n" + "=" * 55)
        print(f"\n- - - Iniciando generación de {tipo_contrato.replace('_', ' ').title()}. - - - \n")
        print("=" * 55)
        datos = solicitar_datos(tipo_contrato)
        if not datos:
            print("\n" + "=" * 55)
            print("\n- - - Generación cancelada debido a errores en los datos. - - -\n")
            print("=" * 55)
            return False
        print("\n" + "=" * 55)
        print("\n- - - Generando contrato... - - -\n")
        print("=" * 55)
        contenido = reemplazar_contenido_contrato(tipo_contrato, datos)
        if contenido:
            print("\n" + "=" * 55)
            print("\n- - - Guardando contrato... - - -\n")
            print("=" * 55)
            archivo_creado = guardar_archivo(contenido, tipo_contrato, datos)
            if archivo_creado:
                print("\n" + "=" * 55)
                print("\n- - - Contrato generado y guardado exitosamente - - -\n")
                print("=" * 55)
                return True
            else:
                print("\n" + "=" * 55)
                print("\n- - - Error al guardar el contrato. - - -\n")
                print("=" * 55)
                return False
        else:
            print("\n" + "=" * 55)
            print("\n- - - Error al generar el contenido del contrato. - - -\n")
            print("=" * 55)
            return False
    except Exception as error:
        error_msg = f"Error en el proceso de generación: {error}"
        print(f"Error: {error_msg}")
        logging.error(error_msg)
        return False

def programa_principal():
    print("\n" + "=" * 55)
    print("\n- - - Bienvenido al Generador de Contratos - Versión 1.0 - - -")
    print("- - - Sistema de gestión de contratos legales. - - -\n")
    print("=" * 55)
    cargar_contratos_desde_registro()
    while True:
        try:
            mostrar_menu_principal()
            opcion = input("\nSeleccione una opción (1-6): ").strip()
            if opcion == '1':
                mostrar_menu_contratos()
                opcion = input("\nSeleccione una opción (1-4): ").strip()
                if opcion == '1':
                    procesar_generacion_contrato('prestacion_servicios')
                elif opcion == '2':
                    procesar_generacion_contrato('arrendamiento')
                elif opcion == '3':
                    procesar_generacion_contrato('compra_venta')
                elif opcion == '4':
                    continue
                else:
                    print("\n" + "=" * 55)
                    print("\n- - - Opción inválida. Por favor seleccione una opción del 1 al 4. - - -\n")
                    print("=" * 55)
            elif opcion == '2':
                ver_contratos_generados()
            elif opcion == '3':
                buscar_contrato()
            elif opcion == '4':
                mostrar_contrato_completo()
            elif opcion == '5':
                editar_contrato()
            elif opcion == '6':
                print("\n" + "=" * 55)
                print("\n- - - Gracias por usar el Generador de Contratos - - -")
                print("- - - Todos los contratos han sido guardados correctamente. - - -\n")
                print("=" * 55)
                break
            else:
                print("\n" + "=" * 55)
                print("\n- - - Opción inválida. Por favor seleccione una opción del 1 al 6. - - -\n")
                print("=" * 55)
            input("\nPresione Enter para continuar...")
        except KeyboardInterrupt:
            print("\n" + "=" * 55)
            print("\n- - - Programa interrumpido por el usuario. - - -\n")
            print("=" * 55)
            confirmacion = input("¿Desea salir? (s/n): ").lower()
            if confirmacion == 's':
                break
        except Exception as error:
            error_msg = f"Error inesperado en el programa principal: {error}"
            print("\n" + "=" * 55)
            print(f"\n- - - Error: {error_msg}. - - -\n")
            print("=" * 55)
            logging.error(error_msg)
            print("\n" + "=" * 55)
            print("\n- - - Intentando continuar... - - -\n")
            print("=" * 55)