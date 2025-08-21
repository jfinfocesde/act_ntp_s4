
def obtener_numeros_pares(lista_numeros):
   
    numeros_pares = []

   
    for numero in lista_numeros:
        
        if numero % 2 == 0:
            numeros_pares.append(numero)  


    return numeros_pares

lista_prueba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = obtener_numeros_pares(lista_prueba)
print("Números pares:", resultado)
