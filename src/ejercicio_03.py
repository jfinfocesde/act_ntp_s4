""" Crea una función que reciba dos listas de igual tamaño y use un ciclo for para combinarlas elemento por elemento en una nueva lista. Ejemplo: [1,2,3] + ['a','b','c'] = [1,'a',2,'b',3,'c']. """

def combinar_listas(lista1, lista2):
    lista_combinada = []

    for i in range(len(lista1)):
        lista_combinada.append(lista1[i])  
        lista_combinada.append(lista2[i]) 

    return lista_combinada

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
resultado = combinar_listas(l1, l2)
print(resultado)

