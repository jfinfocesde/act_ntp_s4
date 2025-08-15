def sistema_calificaciones():
    calificaciones = []
    while True:
        entrada = input("Ingrese calificación o 'fin': ")
        if entrada.lower() == 'fin':
            break
        calificaciones.append(float(entrada))
    print("Promedio:", sum(calificaciones) / len(calificaciones))
    print("Máxima:", max(calificaciones))
    print("Mínima:", min(calificaciones))