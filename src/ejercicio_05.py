def buscar_palabras(palabras):
    letra = input("Letra a buscar: ").lower()
    resultado = []
    for palabra in palabras:
        for caracter in palabra:
            if caracter.lower() == letra:
                resultado.append(palabra)
                break
    return resultado

lista = ["casa", "perro", "gato", "raton"]  
print(buscar_palabras(lista))
