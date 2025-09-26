plantillas_contratos = {        
    'prestacion_servicios': {
        'titulo': 'CONTRATO DE PRESTACIÓN DE SERVICIOS',
        'campos': [
            'nombre_completo_prestador', 'telefono_prestador', 'direccion_prestador',
            'nombre_completo_cliente', 'telefono_cliente', 'direccion_cliente',
            'descripcion_servicio', 'valor_contrato', 'fecha_inicio',
            'fecha_fin', 'forma_pago', 'ciudad'
        ]
    },
    'arrendamiento': {
        'titulo': 'CONTRATO DE ARRENDAMIENTO',
        'campos': [
            'nombre_completo_arrendador', 'telefono_arrendador', 'direccion_arrendador',
            'nombre_completo_arrendatario', 'telefono_arrendatario', 'direccion_arrendatario',
            'direccion_inmueble', 'valor_arriendo', 'valor_deposito',
            'fecha_inicio', 'duracion_meses', 'ciudad'
        ]
    },
    'compra_venta': {
        'titulo': 'CONTRATO DE COMPRA Y VENTA',
        'campos': [
            'nombre_completo_vendedor', 'telefono_vendedor', 'direccion_vendedor',
            'nombre_completo_comprador', 'telefono_comprador', 'direccion_comprador',
            'descripcion_bien', 'valor_bien', 'ciudad', 'fecha_transaccion'
        ]
    }
}