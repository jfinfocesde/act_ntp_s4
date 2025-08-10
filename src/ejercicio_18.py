def agenda():
    contactos = {}
    while True:
        print("\n--- MENÚ AGENDA ---")
        print("1. Agregar contacto")
        print("2. Buscar por nombre")
        print("3. Mostrar todos")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Elige: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            contactos[nombre] = telefono

        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            print(contactos.get(nombre, "No encontrado"))

        elif opcion == "3":
            print(contactos)

        elif opcion == "4":
            nombre = input("Nombre a eliminar: ")
            contactos.pop(nombre, None)

        elif opcion == "5":
            break

agenda()
