import random, math
def coordenadas_aleatorias():
    puntos = tuple((random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(10))
    dentro = [p for p in puntos if math.hypot(p[0], p[1]) <= 5]
    return puntos, dentro
print(coordenadas_aleatorias())