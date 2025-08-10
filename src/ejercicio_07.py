def filtrar_estudiantes(estudiantes):
    return tuple(est for est in estudiantes if est[2] > 8.0)

estudiantes = (("Ana", 20, 9.1), ("Luis", 22, 7.5), ("Marta", 21, 8.5))
print(filtrar_estudiantes(estudiantes))
