
# FUNCION PARA MOSTRAR Y EDITAR CONTRATOS

def mostrar_y_editar_contrato():
    
    # Muestra un contrato por ID y permite editarlo.
    
    # Si no se ingresa id, primero ejecuta la búsqueda
    
    if not contratos_generados:
        print("\nNo hay contratos generados.")
        return

    entrada = input("\nID del contrato (Enter para buscar): ").strip()
    contrato_encontrado = None
    posicion = -1

    if not entrada:
        encontrados = buscar_contratos()
        if not encontrados:
            return
        entrada = input("\nID a abrir: ").strip()

    try:
        id_seleccionado = int(entrada)
    except:
        print("ID inválido.")
        return

    for i, contrato in enumerate(contratos_generados):
        if contrato[0] == id_seleccionado:
            contrato_encontrado = contrato
            posicion = i
            break

    if contrato_encontrado is None:
        print("No se encontró ese ID.")
        return

    id_contrato, tipo, nombre_archivo, cliente, contenido = contrato_encontrado

    print("\n" + "=" * 60)
    print(f"ID: {id_contrato} | Tipo: {tipo.replace('_',' ').title()} | Archivo: {nombre_archivo}")
    print("=" * 60)
    print(contenido)
    print("=" * 60)

    if input("\n¿Editar? (s/n): ").strip().lower() != "s":
        return

    # Pide nuevos datos y regenerar el contrato
    
    if tipo == "prestacion_servicios":
        datos = solicitar_datos("prestacion_servicios")
        nuevo_contenido = generar_contrato_prestacion(datos)
        nuevo_cliente = datos["nombre_cliente"]
    elif tipo == "arrendamiento":
        datos = solicitar_datos("arrendamiento")
        nuevo_contenido = generar_contrato_arrendamiento(datos)
        nuevo_cliente = datos["nombre_arrendatario"]
    else:  # compra_venta
        datos = solicitar_datos("compra_venta")
        nuevo_contenido = generar_contrato_compra_venta(datos)
        nuevo_cliente = datos["nombre_comprador"]

    # Guarda los cambios en archivo y memoria
    
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(nuevo_contenido)
        print(f"Archivo actualizado: {nombre_archivo}")
    except:
        print("No se pudo escribir archivo. Se actualizará en memoria.")

    contratos_generados[posicion] = (id_contrato, tipo, nombre_archivo, nuevo_cliente, nuevo_contenido)
    try:
        actualizar_registro()
    except:
        pass
    print("Contrato actualizado.")
