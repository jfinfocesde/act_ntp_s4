def eliminar_duplicados(lista):
    conjunto = set(lista)
    return conjunto, len(lista) - len(conjunto)
print(eliminar_duplicados([1,1,2,3,3,4]))