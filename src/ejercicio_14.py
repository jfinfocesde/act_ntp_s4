def sistema_votacion():
    votos = set()
    while True:
        v = input("Candidato o 'fin': ")
        if v.lower() == 'fin':
            break
        votos.add(v)
    print("Candidatos votados:", votos)