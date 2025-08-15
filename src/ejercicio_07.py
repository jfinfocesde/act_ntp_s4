def filtrar_estudiantes(estudiantes):
    return tuple(e for e in estudiantes if e[2] > 8.0)
print(filtrar_estudiantes((("Ana", 20, 9.5), ("Luis", 21, 7.8))))