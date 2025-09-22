from  estructuras_contratos import *
def generar_contrato_prestacion(datos):
    """Genera el contenido del contrato de prestación de servicios."""
    fecha_actual = obtener_fecha_actual()
    contrato = f"""
{estructuras_contratos['prestacion_servicios']['titulo']}

Entre los suscritos a saber: {datos['nombre_prestador']}, identificado(a) con 
cédula de ciudadanía No. {datos['cedula_prestador']}, domiciliado(a) en 
{datos['direccion_prestador']}, quien en adelante se denominará EL PRESTADOR, 
y {datos['nombre_cliente']}, identificado(a) con cédula de ciudadanía 
No. {datos['cedula_cliente']}, domiciliado(a) en {datos['direccion_cliente']}, 
quien en adelante se denominará EL CLIENTE, hemos convenido celebrar el 
presente contrato de prestación de servicios.

Dado en {datos['ciudad']}, a los {fecha_actual}
...
"""
    return contrato