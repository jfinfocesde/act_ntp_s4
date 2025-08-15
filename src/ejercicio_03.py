def combinar_listas(lista1, lista2):
    combinada = []
    for i in range(len(lista1)):
        combinada.append(lista1[i])
        combinada.append(lista2[i])
    return combinada
print(combinar_listas([1, 2, 3], ['a', 'b', 'c']))