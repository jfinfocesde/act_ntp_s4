def generar_conjuntos():
    pares = {i for i in range(2, 21, 2)}
    multiplos_3 = {i for i in range(3, 31, 3)}
    print("Pares:", pares)
    print("Múltiplos de 3:", multiplos_3)
    print("Unión:", pares | multiplos_3)
    print("Intersección:", pares & multiplos_3)
    print("Diferencia:", pares - multiplos_3)

generar_conjuntos()
