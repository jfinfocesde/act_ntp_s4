def inventario():
    inv = {}
    while True:
        op = input("1.Agregar 2.Actualizar 3.Eliminar 4.Mostrar 5.Salir: ")
        if op == '1':
            prod = input("Producto: ")
            cant = int(input("Cantidad: "))
            inv[prod] = cant
        elif op == '2':
            prod = input("Producto: ")
            cant = int(input("Cantidad: "))
            inv[prod] = cant
        elif op == '3':
            prod = input("Producto: ")
            inv.pop(prod, None)
        elif op == '4':
            print(inv)
        elif op == '5':
            break