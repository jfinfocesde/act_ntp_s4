def filtrar_pares(lista_numeros):
    pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares
print(filtrar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))