# Crear un diccionario para almacenar información de las agrupaciones musicales
bandas = {}

# Menú de opciones
while True:
    print("\nMenú de opciones:")
    print("1. Registrar una banda")
    print("2. Mostrar bandas no presentadas")
    print("3. Cambiar hora de presentación")
    print("4. Retirar una banda")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion (RegistrarBanda) == '1':
        id_banda = input("Ingrese el ID de la banda: ")
        nombre = input("Ingrese el nombre de la banda: ")
        genero = input("Ingrese el género de la banda: ")
        hora_presentacion = input("Ingrese la hora de presentación de la banda: ")
        pago = float(input("Ingrese el pago para la banda: "))
        estado = False  # Inicialmente, la banda no se ha presentado
        bandas[id_banda] = {'nombre': nombre, 'genero': genero, 'hora_presentacion': hora_presentacion, 'pago': pago, 'estado': estado}
        print(f"Banda '{nombre}' registrada con éxito.")
    elif opcion == '2':
        print("Bandas que no se han presentado:")
        for id_banda, banda in bandas.items():
            if not banda['estado']:
                print(f"ID: {id_banda}, Nombre: {banda['nombre']}, Género: {banda['genero']}, Hora de presentación: {banda['hora_presentacion']}")
    elif opcion == '3':
        id_banda = input("Ingrese el ID de la banda cuya hora de presentación desea cambiar: ")
        if id_banda in bandas and not bandas[id_banda]['estado']:
            nueva_hora = input("Ingrese la nueva hora de presentación: ")
            bandas[id_banda]['hora_presentacion'] = nueva_hora
            print(f"Hora de presentación de la banda '{bandas[id_banda]['nombre']}' actualizada con éxito.")
        else:
            print("La banda no existe o ya se ha presentado.")
    elif opcion == '4':
        id_banda = input("Ingrese el ID de la banda que desea retirar: ")
        if id_banda in bandas and not bandas[id_banda]['estado']:
            del bandas[id_banda]
            print("Banda retirada con éxito.")
        else:
            print("La banda no existe o ya se ha presentado.")
    elif opcion == '5':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
