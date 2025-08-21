def gestion_calificaciones():
    calificaciones = {}
    while True:
        op = input("1.Agregar estudiante 2.Agregar nota 3.Promedio 4.Salir: ")
        if op == '1':
            est = input("Nombre: ")
            calificaciones[est] = []
        elif op == '2':
            est = input("Nombre: ")
            nota = float(input("Nota: "))
            calificaciones[est].append(nota)
        elif op == '3':
            for est, notas in calificaciones.items():
                print(est, sum(notas)/len(notas) if notas else 0)
        elif op == '4':
            break