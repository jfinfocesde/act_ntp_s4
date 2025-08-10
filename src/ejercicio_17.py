def contador_palabras(frase):
    palabras = frase.lower().split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    for palabra, cantidad in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
        print(f"{palabra}: {cantidad}")

contador_palabras("Hola hola mundo mundo mundo")
