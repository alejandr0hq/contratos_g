#Generador de contratos
#Estas son las variables 
Nombre_Part_de_contrato1 = ""
Nombre_Part_de_contrato2 = ""
Dirección = ""
Fecha = 0
Cliente = ""
Costo_de_arrendamientos = ""
Servicio = ""
Ubicacion = ""
Fecha_Incio = ""
Fecha_Salida = ""

#Este es el menu del generador de contratos
print("=========== Generador de contratos legales===========: ")
opcion = ""
#Aqui entramos al ciclo while
while opcion != "3": 
    print("=========\nMenu=========")
    print("1. Mostrar el contrato de arrendamiento: ")
    print("2. Mostrar el contrato de prestacion de servicios: ")
    print("3. Salir del generador de contratos: ")
#Pedimos Datos
    opcion = (input("Elija una opcion: "))

    if opcion == "1":
       Fecha = int(input("Ingrese Fecha para el contrato: "))
       Nombre_Part_de_contrato1 = (input("Ingrese Nombre del contrato (Arrendamientos): "))
       Costo_de_arrendamientos = (input("Ingrese la cantidad en pesos: "))
       Ubicacion = (input("Ingrese la Ubicacion del contrato de arrendamiento: "))
       Costo_de_arrendamientos = int(input("Ingrese Costo del contrato de arrendamiento: "))
       Fecha_Incio=  int(input("Ingrese Fecha de Inicio del contrarto: "))
       Fecha_Salida = int(input("Ingrese Fecha de Final del contrato: "))
       print("Mostrar Datos del contrato de arrendamientos: ")
    elif opcion == "2":
        print("Fin del programa Beta de generador contratos: ")









