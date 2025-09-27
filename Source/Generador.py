from .Fecha import fecha
from .Plantillas import plantillas_contratos

def reemplazar_contenido_contrato(tipo_contrato, datos):
    fecha_actual = fecha()
    
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

Dado en {ciudad}, el dia {fecha_actual}



______________________________            ______________________________
{parte1_rol_mayuscula:^30}            {parte2_rol_mayuscula:^30}
{parte1_nombre:^30}            {parte2_nombre:^30}
Teléfono: {parte1_telefono:^20}            Teléfono: {parte2_telefono:^20}
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

    return template_base.format(**config)