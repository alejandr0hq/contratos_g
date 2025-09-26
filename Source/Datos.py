from .Plantillas import plantillas_contratos
from .Validaciones import validar_entrada
from .Logger import logging

def solicitar_datos(tipo_contrato):
    datos = {}
    plantilla = plantillas_contratos[tipo_contrato]
    print("\n" + "=" * 55)
    print(f"\n- - - DATOS PARA {plantilla['titulo']}. - - -\n")
    print("=" * 55)
    for campo in plantilla['campos']:
        max_intentos = 5
        valor_valido = None
        for intento in range(max_intentos):
            try:
                campo_formateado = campo.replace('_', ' ').title()
                if 'fecha' in campo.lower():
                    prompt = f"{campo_formateado} (DD/MM/AAAA): "
                else:
                    prompt = f"{campo_formateado}: "
                valor = input(prompt).strip()
                if not any(x in campo.lower() for x in ['valor', 'telefono', 'fecha', 'deposito', 'duracion', 'mes']):
                    valor = valor.title()
                if validar_entrada(campo, valor):
                    valor_valido = valor
                    break
                else:
                    print("\n" + "=" * 55)
                    print(f"\n- - - Intento {intento + 1} de {max_intentos}. - - -\n")
                    print("=" * 55)
            except KeyboardInterrupt:
                print("\n" + "=" * 55)
                print("\n- - - Operación cancelada por el usuario. - - -\n")
                print("=" * 55)
                return None
            except Exception as error:
                logging.error(f"Error inesperado al procesar entrada para {campo}: {error}")
                print("\n" + "=" * 55)
                print("\n- - - Error inesperado al procesar la entrada. - - -\n")
                print("=" * 55)
        if valor_valido is None:
            print("\n" + "=" * 55)
            print(f"\n- - - Demasiados intentos fallidos para el campo {campo_formateado}. - - -\n")
            print("=" * 55)
            return None
        datos[campo] = valor_valido
    return datos