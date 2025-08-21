def buscar_palabras(lista_palabras, letra):
    resultado = []
    for palabra in lista_palabras:
        if letra in palabra:
            resultado.append(palabra)
    return resultado
print(buscar_palabras(['hola', 'mundo', 'python'], 'o'))