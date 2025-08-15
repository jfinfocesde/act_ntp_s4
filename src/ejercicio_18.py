def agenda():
    contactos = {}
    while True:
        op = input("1.Agregar 2.Buscar 3.Mostrar 4.Eliminar 5.Salir: ")
        if op == '1':
            nombre = input("Nombre: ")
            tel = input("Teléfono: ")
            contactos[nombre] = tel
        elif op == '2':
            nombre = input("Nombre: ")
            print(contactos.get(nombre, "No encontrado"))
        elif op == '3':
            print(contactos)
        elif op == '4':
            nombre = input("Nombre: ")
            contactos.pop(nombre, None)
        elif op == '5':
            break