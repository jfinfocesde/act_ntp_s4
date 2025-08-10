def operaciones_conjuntos(l1, l2):
    c1 = set(l1)
    c2 = set(l2)
    print("Unión:", c1 | c2)
    print("Intersección:", c1 & c2)
    print("Diferencia:", c1 - c2)
    print("Diferencia simétrica:", c1 ^ c2)

operaciones_conjuntos([1,2,3], [3,4,5])
