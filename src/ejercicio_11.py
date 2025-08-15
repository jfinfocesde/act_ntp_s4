def operaciones_conjuntos(l1, l2):
    c1, c2 = set(l1), set(l2)
    return c1|c2, c1&c2, c1-c2, c1^c2
print(operaciones_conjuntos([1,2,3],[3,4,5]))
