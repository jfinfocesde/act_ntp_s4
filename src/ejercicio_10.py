def sumar_tuplas(t1, t2):
    return tuple(t1[i] + t2[i] for i in range(len(t1)))

print(sumar_tuplas((1,2,3), (4,5,6)))
