# Función que solicita calificaciones al usuario hasta que escriba 'fin'
# Luego calcula el promedio, la nota más alta y la más baja
def procesar_calificaciones():
    # Lista para almacenar las calificaciones ingresadas
    calificaciones = []

    while True:
        # Solicitamos al usuario una calificación o la palabra 'fin'
        entrada = input("Ingresa una calificación (o escribe 'fin' para terminar): ")

        # Condición de salida
        if entrada.lower() == 'fin':
            break

        # Intentamos convertir la entrada a número (float)
        try:
            nota = float(entrada)
            # Validamos que la nota esté en el rango 0-100
            if 0 <= nota <= 100:
                calificaciones.append(nota)
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número o 'fin'.")

    # Verificamos si se ingresaron calificaciones
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        nota_maxima = max(calificaciones)
        nota_minima = min(calificaciones)

        # Mostramos los resultados
        print("\nResumen de calificaciones:")
        print("Calificaciones ingresadas:", calificaciones)
        print("Promedio:", round(promedio, 2))
        print("Nota más alta:", nota_maxima)
        print("Nota más baja:", nota_minima)
    else:
        print("No se ingresaron calificaciones.")

# Llamamos a la función
procesar_calificaciones()
