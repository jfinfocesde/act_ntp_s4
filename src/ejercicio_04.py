def carrito_compras():
    carrito = []
    while True:
        opcion = input("1.Agregar 2.Eliminar 3.Mostrar 4.Total 5.Salir: ")
        if opcion == '1':
            producto = input("Producto: ")
            precio = float(input("Precio: "))
            carrito.append((producto, precio))
        elif opcion == '2':
            producto = input("Producto a eliminar: ")
            carrito = [p for p in carrito if p[0] != producto]
        elif opcion == '3':
            print(carrito)
        elif opcion == '4':
            print("Total:", sum(p[1] for p in carrito))
        elif opcion == '5':
            break