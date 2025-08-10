def palabras_unicas():
    palabras = set()
    repetidas = set()
    while True:
        palabra = input("Ingresa palabra (o 'salir'): ").lower()
        if palabra == "salir":
            break
        if palabra in palabras:
            repetidas.add(palabra)
        palabras.add(palabra)
    print(f"Palabras únicas: {len(palabras)}")
    print("Repetidas:", repetidas)

palabras_unicas()
