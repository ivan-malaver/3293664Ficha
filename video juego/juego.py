from moto import crear_moto
from menu import mostrar_opciones

def jugar():
    motos = []
    while True:
        opcion = mostrar_opciones()
        if opcion == "1":
            marca = input("tvs", "bajaj", "hero", "honda", "yamaha", "suzuki", "ktm", "ducati", "harley-davidson")
            modelo = input("2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023")
            color = input("rojo", "azul","negro", "blanco", "verde", "amarillo", "gris", "morado", "naranja", "rosa")
            cilindraje = input("110", "125", "150", "200", "250", "300", "400", "500", "600", "1000")
            moto = crear_moto(marca, modelo, color, cilindraje)
            motos.append(moto)
            print("Moto creada exitosamente.")

        print("Bienvenido a el juego de creación de motos!")
marcas = mostrar_opciones("Por favor, ingresa tu nombre: ")
modelos = mostrar_opciones("Por favor, ingresa el modelo de la moto que deseas crear (2014-2023): ")
colores = mostrar_opciones("Por favor, ingresa el color de la moto que deseas crear:")
cilindrajes = mostrar_opciones("Por favor, ingresa el cilindraje de la moto que deseas crear (110-1000): ")

moto = crear_moto(marcas, modelos, colores, cilindrajes)