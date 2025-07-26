""" Implementa una función que solicite al usuario ingresar calificaciones usando un ciclo while hasta que escriba 'fin'. Almacena las calificaciones en una lista y calcula el promedio, la nota más alta y más baja.
 """
def Calificaciones():
    calificaciones = []
    
    while True:
        nota = input("Ingrese una calificación o 'fin' para terminar: ")
        if nota.lower() == "fin":
            break
        try:
            calificaciones = float(nota)
            calificaciones.append(calificaciones)
        except ValueError:
            print ("El valor digitado no es valido. Intente de nuevo.")

