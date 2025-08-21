# Función principal que simula un carrito de compras
def carrito_de_compras():
    # Lista para almacenar los productos del carrito
    carrito = []

    # Menú interactivo dentro de un ciclo while
    while True:
        print("\n--- Menú del Carrito de Compras ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar productos")
        print("4. Calcular total")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        # Opción 1: Agregar producto al carrito
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                # Agregamos el producto como un diccionario
                producto = {"nombre": nombre, "precio": precio}
                carrito.append(producto)
                print(f" Producto '{nombre}' agregado correctamente.")
            except ValueError:
                print(" Precio inválido. Intenta de nuevo.")

        # Opción 2: Eliminar producto por nombre
        elif opcion == '2':
            nombre = input("Nombre del producto a eliminar: ")
            encontrado = False
            # Buscamos el producto en el carrito
            for producto in carrito:
                if producto["nombre"].lower() == nombre.lower():
                    carrito.remove(producto)
                    print(f" Producto '{nombre}' eliminado.")
                    encontrado = True
                    break
            if not encontrado:
                print(f" Producto '{nombre}' no encontrado en el carrito.")

        # Opción 3: Mostrar productos en el carrito
        elif opcion == '3':
            if not carrito:
                print(" El carrito está vacío.")
            else:
                print("\n Productos en el carrito:")
                for idx, producto in enumerate(carrito, start=1):
                    print(f"{idx}. {producto['nombre']} - ${producto['precio']:.2f}")

        # Opción 4: Calcular el total
        elif opcion == '4':
            total = sum(producto["precio"] for producto in carrito)
            print(f" Total a pagar: ${total:.2f}")

        # Opción 5: Salir del programa
        elif opcion == '5':
            print(" Gracias por usar el carrito de compras.")
            break

        # Opción inválida
        else:
            print(" Opción no válida. Por favor, elige entre 1 y 5.")

# Llamamos a la función para ejecutar el carrito
carrito_de_compras()
