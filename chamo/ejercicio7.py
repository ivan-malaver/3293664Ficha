
precio_total=17000
iva=0.16
#Realizar la operacion
if precio_total >16000:
    total=precio_total*iva
    print(f"Este tu precio con iva, {total}")
#precio sin iva
elif precio_total >25000:
    total=precio_total*iva
    print(f"Este es tu precio sin iva, {total}")
else:
    print(f"Este precio no es valido")