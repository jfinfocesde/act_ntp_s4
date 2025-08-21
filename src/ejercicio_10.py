def suma_tuplas(t1, t2):
    return tuple(t1[i] + t2[i] for i in range(len(t1)))
print(suma_tuplas((1,2,3),(4,5,6)))
