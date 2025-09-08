def mostrar_opciones(titulo, opciones):
    print(titulo)
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
    eleccion = int(input("Selecciona una opción: "))
    return opciones[int(eleccion) - 1]
    