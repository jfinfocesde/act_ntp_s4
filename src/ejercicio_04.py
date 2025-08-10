def carrito_compras():
    carrito = []
    while True:
        print("MENÚ CARRITO DE COMPRAS")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar productos")
        print("4. Calcular total")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            producto = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            carrito.append((producto, precio))
            print(f"{producto} agregado.")

        elif opcion == "2":
            producto = input("Producto a eliminar: ")
            carrito = [p for p in carrito if p[0] != producto]
            print(f"{producto} eliminado (si existía).")

        elif opcion == "3":
            if carrito:
                for p, precio in carrito:
                    print(f"{p} - ${precio:.2f}")
            else:
                print("Carrito vacío.")

        elif opcion == "4":
            total = sum(precio for _, precio in carrito)
            print(f"Total: ${total:.2f}")

        elif opcion == "5":
            break

        else:
            print("Opción no válida.")

carrito_compras()
