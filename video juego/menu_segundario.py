from moto import jugar

moto=jugar()
print( "moto creada exitosamente")
print("Es una moto de un miltimillonario que se llama Elon Musk")
for clave, valor in moto.items():
    print(f"{clave}: {valor}")