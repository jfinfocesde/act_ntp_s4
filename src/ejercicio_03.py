# Función que recibe dos listas del mismo tamaño y las combina alternando sus elementos
def combinar_listas(lista1, lista2):
    # Verificamos que ambas listas tengan el mismo tamaño
    if len(lista1) != len(lista2):
        print("Error: Las listas deben tener el mismo tamaño.")
        return []

    # Lista para almacenar el resultado combinado
    lista_combinada = []

    # Recorremos los índices de las listas usando un ciclo for
    for i in range(len(lista1)):
        lista_combinada.append(lista1[i])  # Agregamos el elemento de la primera lista
        lista_combinada.append(lista2[i])  # Agregamos el elemento correspondiente de la segunda lista

    # Devolvemos la lista combinada
    return lista_combinada

# Prueba de la función con listas de ejemplo
lista_numeros = [1, 2, 3]
lista_letras = ['a', 'b', 'c']

resultado = combinar_listas(lista_numeros, lista_letras)
print("Lista combinada:", resultado)
