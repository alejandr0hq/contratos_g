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

print("===========Generador de contratos legales===========\n ")
#Aqui imprimimos el nombre del programa

opcion = ""

#Aqui entramos al ciclo while

while opcion != "3": 
    print("\t=========Menu=========\n")
    print("1. Contrato de Arrendamiento: ")
    print("2. Contrato de Prestacion de Servicios: ")
    print("3. Salir del generador de contratos :\n ")
    
#Solicitamos Datos

    opcion = (input("Elija una opcion: "))
#Aqui tenemos la condición

    if opcion == "1":
       Fecha = (input("Ingrese Fecha para el contrato: \n"))
       Nombre_Part_de_contrato1 = (input("Ingrese Nombre del Arrendador :\n "))
       Nombre_Part_de_contrato2 = (input("Ingrese el nombre del Arrendatario :\n "))
       Costo_de_arrendamientos = (input("Ingrese la cantidad en pesos MX : $ "))
       Ubicacion = (input("Ingrese la Ubicacion del inmueble :\n "))
       Fecha_Incio=  (input("Ingrese Fecha de Inicio del contrarto:\n "))
       Fecha_Salida = (input("Ingrese Fecha de Final del contrato:\n "))
       
       print("\n#Aqui se va a mostrar el contrato completo")
       
    #Aqui se solicitaran los datos del contrato #2
    
    elif opcion == "2":
        print("Contrato no disponible")
        
    #Aqui se termina el programa
    
    elif opcion == 3 :
        break
    print("Fin del programa")









