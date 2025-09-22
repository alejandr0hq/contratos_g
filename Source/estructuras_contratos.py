estructuras_contratos = {
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
    },
    'compra_venta': {
        'titulo': 'CONTRATO DE COMPRA Y VENTA',
        'campos': [
            'nombre_vendedor', 'cedula_vendedor', 'direccion_vendedor',
            'nombre_comprador', 'cedula_comprador', 'direccion_comprador',
            'descripcion_bien', 'valor_bien', 'ciudad', 'fecha_transaccion'
        ]
    }
}
contratos_generados = []
contador_contratos = 1