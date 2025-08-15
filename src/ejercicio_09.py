import math
def distancia_total(puntos):
    distancia = 0
    for i in range(len(puntos) - 1):
        distancia += math.dist(puntos[i], puntos[i+1])
    return distancia
print(distancia_total(((0,0),(3,4),(6,8))))