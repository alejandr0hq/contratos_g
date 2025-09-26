from .Logger import logging

def validar_nombre(nombre):
    if not nombre or len(nombre.strip()) < 2:
        return False
    return True

def validar_telefono(telefono):
    if len(telefono) < 9 or len(telefono) > 13:
        return False
    return True

def validar_precio(precio_str):
    try:
        valor = float(precio_str.replace(',', '').replace('.', ''))
        return valor > 0
    except ValueError:
        return False

def validar_entrada(campo, valor):
    try:
        valor = valor.strip()
        if not valor:
            raise ValueError("Este campo no puede estar vacío.")
        if 'nombre' in campo.lower():
            if not validar_nombre(valor):
                raise ValueError("El nombre debe contener solo letras y espacios, mínimo 2 caracteres. ")
        elif 'telefono' in campo.lower():
            if not validar_telefono(valor):
                raise ValueError("El teléfono debe tener entre 9 y 12 dígitos numéricos.")
        elif 'valor' in campo.lower() or 'deposito' in campo.lower():
            if not validar_precio(valor):
                raise ValueError("El valor debe ser un número mayor a 0.")
        elif 'duracion' in campo.lower() and 'mes' in campo.lower():
            try:
                meses = int(valor)
                if meses <= 0 or meses > 180:
                    raise ValueError("La duración debe ser entre 1 y 180 meses.")
            except ValueError:
                raise ValueError("La duración debe ser un número entero.")
        elif len('fecha_inicio') < 10 or len('fecha_fin') > 10:
            raise ValueError("La fecha debe contener el formato (DD/MM/AAAA).")
        return True
    except ValueError as error:
        print("\n" + "=" * 55)
        print(f"\n- - - Error de validación: {error}. - - -\n")
        print("=" * 55)
        return False