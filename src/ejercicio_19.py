def gestion_calificaciones():
    calificaciones = {}
    while True:
        print("\n--- MENÚ CALIFICACIONES ---")
        print("1. Agregar estudiante")
        print("2. Agregar calificación")
        print("3. Calcular promedio")
        print("4. Salir")
        opcion = input("Elige: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            calificaciones[nombre] = []

        elif opcion == "2":
            nombre = input("Estudiante: ")
            if nombre in calificaciones:
                nota = float(input("Calificación: "))
                calificaciones[nombre].append(nota)

        elif opcion == "3":
            for nombre, notas in calificaciones.items():
                if notas:
                    promedio = sum(notas) / len(notas)
                    print(f"{nombre}: {promedio:.2f}")
                else:
                    print(f"{nombre}: Sin calificaciones")

        elif opcion == "4":
            break

gestion_calificaciones()
