from estructuras_contratos import *
def generar_contrato_compra_venta(datos):
    """Genera el contenido del contrato de compra y venta."""
    fecha_actual = obtener_fecha_actual()
    contrato = f"""
{estructuras_contratos['compra_venta']['titulo']}

Entre los suscritos a saber: {datos['nombre_vendedor']}, identificado(a) con
cédula de ciudadanía No. {datos['cedula_vendedor']}, domiciliado(a) en
{datos['direccion_vendedor']}, quien en adelante se denominará EL VENDEDOR,
y {datos['nombre_comprador']}, identificado(a) con cédula de ciudadanía
No. {datos['cedula_comprador']}, domiciliado(a) en {datos['direccion_comprador']},
quien en adelante se denominará EL COMPRADOR, hemos convenido celebrar el
presente contrato de compra y venta.

Dado en {datos['ciudad']}, a los {fecha_actual}
...
"""
    return contrato