def sistema_temperaturas():
    ciudades = {}
    while True:
        ciudad = input("Ciudad (o 'fin'): ")
        if ciudad.lower() == "fin":
            break
        dias = {}
        for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
            temp = float(input(f"Temperatura {dia}: "))
            dias[dia] = temp
        ciudades[ciudad] = dias

    for ciudad, temps in ciudades.items():
        promedio = sum(temps.values()) / len(temps)
        print(f"{ciudad}: Promedio {promedio:.2f}°C")

sistema_temperaturas()
