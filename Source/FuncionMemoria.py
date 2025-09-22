def guardar_contrato_memoria(contenido, tipo, datos):
    """Función de respaldo: guarda solo en memoria si no se puede crear archivo"""
    global contador_contratos
    
    try:
        if tipo == 'prestacion_servicios':
            cliente = datos['nombre_cliente']
        elif tipo == 'arrendamiento':
            cliente = datos['nombre_arrendatario']
        else:
            cliente = datos['nombre_comprador']
        
        nombre_archivo = f"{tipo}_{cliente.replace(' ', '_')}_{str(contador_contratos)}.txt"
        
        info_contrato = (contador_contratos, tipo, nombre_archivo, cliente, contenido)
        contratos_generados.append(info_contrato)
        
        print(f"\nContrato generado exitosamente con ID: {str(contador_contratos)}")
        print("(Guardado solo en memoria)")
        
        contador_contratos += 1
        return nombre_archivo