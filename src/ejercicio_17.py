def contador_palabras(frase):
    palabras = frase.lower().split()
    contador = {}
    for p in palabras:
        contador[p] = contador.get(p, 0) + 1
    return dict(sorted(contador.items(), key=lambda x: x[1], reverse=True))
print(contador_palabras("Hola hola mundo mundo mundo"))