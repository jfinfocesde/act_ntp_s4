# Función que recibe una lista de palabras y devuelve las que contienen una letra dada por el usuario
def buscar_palabras_por_letra(lista_palabras):
    # Pedimos al usuario que ingrese la letra a buscar
    letra = input("Ingresa la letra que deseas buscar: ").lower()

    # Lista para almacenar palabras que contienen la letra
    palabras_encontradas = []

    # Recorremos cada palabra de la lista
    for palabra in lista_palabras:
        # Recorremos cada letra dentro de la palabra (ciclo anidado)
        for caracter in palabra:
            # Comparamos en minúsculas para no diferenciar entre mayúsculas y minúsculas
            if caracter.lower() == letra:
                palabras_encontradas.append(palabra)
                break  # Salimos del ciclo interno si ya encontramos la letra en la palabra

    # Devolvemos la lista de palabras que contienen la letra
    return palabras_encontradas

# Lista de prueba
lista = ["gato", "perro", "ratón", "jirafa", "elefante", "pez"]

# Llamamos a la función y mostramos el resultado
resultado = buscar_palabras_por_letra(lista)
print(" Palabras que contienen la letra buscada:", resultado)
