def sistema_votacion():
    votos = set()
    while True:
        voto = input("Vota por un candidato (o 'fin'): ").lower()
        if voto == "fin":
            break
        votos.add(voto)
    print("Candidatos con votos:", votos)

sistema_votacion()
