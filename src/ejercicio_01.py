""" Crea una función que reciba una lista de números y use un ciclo for para devolver una nueva lista con solo los números pares. Prueba la función con la lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
 """
def filtrar_pares(numeros):
    """Filtra los números pares de una lista."""
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares
