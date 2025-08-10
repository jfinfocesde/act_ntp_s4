import random
import math

def coordenadas():
    puntos = tuple((random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(10))
    dentro = []
    for x, y in puntos:
        if math.sqrt(x**2 + y**2) <= 5:
            dentro.append((x, y))
    return puntos, dentro

print(coordenadas())
