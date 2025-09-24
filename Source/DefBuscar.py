
# FUNCION PARA BUSCAR CONTRATOS

def buscar_contratos():
    
    # Búsqueda por nombre de cliente, archivo o tipo.
    
    # Coincidencia mayúsculas y minúsculas.
    
    if not contratos_generados:
        print("\nNo hay contratos generados.")
        return []

    consulta = input("\nBuscar (cliente/archivo/tipo): ").strip().lower()
    resultados = []
    for contrato in contratos_generados:
        id_contrato, tipo, archivo, cliente, _ = contrato
        texto = f"{cliente} {archivo} {tipo}".lower()
        if consulta in texto:
            resultados.append(contrato)

    if resultados:
        print(f"\nResultados ({len(resultados)}):")
        print("ID | Tipo                | Cliente              | Archivo")
        print("-" * 62)
        for id_contrato, tipo, archivo, cliente, _ in resultados:
            print(f"{id_contrato} | {tipo:<19} | {cliente[:18]:<18} | {archivo[:20]}"
                  f"{cliente[:18]:<18} | {archivo[:20]}")
    else:
        print("\nSin coincidencias.")
    return resultados
