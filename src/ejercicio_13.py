def generar_conjuntos():
    pares = {n for n in range(2, 21, 2)}
    multiplos3 = {n for n in range(3, 31, 3)}
    return pares, multiplos3, pares|multiplos3, pares&multiplos3, pares-multiplos3, pares^multiplos3
print(generar_conjuntos())