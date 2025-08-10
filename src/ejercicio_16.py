def inventario():
    productos = {}
    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Actualizar cantidad")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Elige: ")

        if opcion == "1":
            nombre = input("Producto: ")
            cantidad = int(input("Cantidad: "))
            productos[nombre] = cantidad

        elif opcion == "2":
            nombre = input("Producto a actualizar: ")
            if nombre in productos:
                cantidad = int(input("Nueva cantidad: "))
                productos[nombre] = cantidad

        elif opcion == "3":
            nombre = input("Producto a eliminar: ")
            productos.pop(nombre, None)

        elif opcion == "4":
            print(productos)

        elif opcion == "5":
            break

inventario()
