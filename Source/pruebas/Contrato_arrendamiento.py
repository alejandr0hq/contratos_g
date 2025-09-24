# Importar desde otros archivos
from Fecha import fecha
from Datos import plantillas_contratos

# Función que llena el contrato
def contrato_arrendamiento ( datos ) :
    fecha_actual = fecha ( )
    contrato = f"""
{plantillas_contratos['arrendamiento']['titulo']}

Entre los suscritos a saber: {datos['nombre_arrendador']}, identificado(a) con 
cédula de ciudadanía No. {datos['cedula_arrendador']}, domiciliado(a) en 
{datos['direccion_arrendador']}, quien en adelante se denominará EL ARRENDADOR, 
y {datos['nombre_arrendatario']}, identificado(a) con cédula de ciudadanía 
No. {datos['cedula_arrendatario']}, domiciliado(a) en {datos['direccion_arrendatario']}, 
quien en adelante se denominará EL ARRENDATARIO, hemos convenido celebrar el 
presente contrato de arrendamiento.

CLÁUSULAS:

PRIMERA - OBJETO: El arrendador entrega en arrendamiento al arrendatario el 
inmueble ubicado en: {datos['direccion_inmueble']}

SEGUNDA - VALOR: El canon mensual de arrendamiento es de ${datos['valor_arriendo']} 
pesos, que se pagará dentro de los primeros cinco (5) días de cada mes.

TERCERA - DEPÓSITO: El arrendatario entrega como depósito de garantía la suma de 
${datos['valor_deposito']} pesos.

CUARTA - DURACIÓN: El presente contrato tendrá una duración de {datos['duracion_meses']} 
meses, contados a partir del {datos['fecha_inicio']}.

QUINTA - OBLIGACIONES: Las partes se comprometen a cumplir con las obligaciones 
establecidas por la ley y este contrato.

Dado en {datos['ciudad']}, a los {fecha_actual}

_________________________          _________________________
EL ARRENDADOR                        EL ARRENDATARIO
{datos['nombre_arrendador']}          {datos['nombre_arrendatario']}
C.C. {datos['cedula_arrendador']}     C.C. {datos['cedula_arrendatario']}
"""
    return contrato