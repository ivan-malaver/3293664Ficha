# Detector de números impares
numero = 1       
limite = 10     # Hasta dónde buscar
impares_encontrados = 0  

print("Buscando números impares entre 1 y", limite, ":")

while numero <= limite:
    if numero % 2 != 0:  
        print(numero, "es impar")
        impares_encontrados = impares_encontrados + 1
    numero = numero + 1  

print("Se encontraron", impares_encontrados, "impares")
