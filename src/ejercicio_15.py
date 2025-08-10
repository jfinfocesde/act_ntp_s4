def eliminar_duplicados(lista):
    conjunto = set(lista)
    duplicados = len(lista) - len(conjunto)
    print("Números únicos:", conjunto)
    print("Duplicados:", duplicados)

eliminar_duplicados([1,2,2,3,4,4,4,5])
