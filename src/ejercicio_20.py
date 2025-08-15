def sistema_temperaturas():
    temps = {}
    while True:
        op = input("1.Agregar ciudad 2.Agregar temp 3.Mostrar 4.Salir: ")
        if op == '1':
            ciudad = input("Ciudad: ")
            temps[ciudad] = {}
        elif op == '2':
            ciudad = input("Ciudad: ")
            dia = input("Día: ")
            temp = float(input("Temperatura: "))
            temps[ciudad][dia] = temp
        elif op == '3':
            for c, dias in temps.items():
                print(c, dias)
        elif op == '4':
            break