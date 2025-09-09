# Juego de adivinanza de marca de moto
moto_secreta = "Yamaha"
intentos_maximos = 3
intento_actual = 1

print("Adivinar la moto secreta!")
print("Tienes", intentos_maximos, "intentos para adivinar la moto (Yamaha, Honda, KTM, Ducati)")

while intento_actual <= intentos_maximos:
    print("\nIntento", intento_actual, "de", intentos_maximos)
    
    # Escribe la adivinanza
    adivinanza = input("Escribe tu adivinanza: ")

    if adivinanza == moto_secreta:
        print("¡GANASTE! La moto secreta era", moto_secreta)
        
    else:
        print("No es crack. Intenta de nuevo.")
    
    intento_actual += 1

if intento_actual > intentos_maximos:
    print(" Se acabaron los intentos. La moto secreta era:", moto_secreta)
