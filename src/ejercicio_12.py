def palabras_unicas():
    palabras = set()
    repetidas = set()
    while True:
        p = input("Palabra o 'salir': ")
        if p.lower() == 'salir':
            break
        if p in palabras:
            repetidas.add(p)
        palabras.add(p)
    print("Únicas:", len(palabras))
    print("Repetidas:", repetidas)