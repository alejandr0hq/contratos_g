
from estructuras_contratos import *
def generar_contrato_arrendamiento(datos):
    """Genera el contenido del contrato de arrendamiento."""
    fecha_actual = obtener_fecha_actual()
    contrato = f"""
{estructuras_contratos['arrendamiento']['titulo']}

Entre los suscritos a saber: {datos['nombre_arrendador']}, identificado(a) con 
cédula de ciudadanía No. {datos['cedula_arrendador']}, domiciliado(a) en 
{datos['direccion_arrendador']}, quien en adelante se denominará EL ARRENDADOR, 
y {datos['nombre_arrendatario']}, identificado(a) con cédula de ciudadanía 
No. {datos['cedula_arrendatario']}, domiciliado(a) en {datos['direccion_arrendatario']}, 
quien en adelante se denominará EL ARRENDATARIO, hemos convenido celebrar el 
presente contrato de arrendamiento.

Dado en {datos['ciudad']}, a los {fecha_actual}
...
"""
    return contrato