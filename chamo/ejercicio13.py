    # Multiplicador acumulativo
producto_total = 1       # Empezamos en 1 
numero_actual = 1        
limite = 5           

print("Multiplicando números del 1 al", limite,)

while numero_actual <= limite:
    producto_total = producto_total * numero_actual  
    print("Multiplicando por", numero_actual, "- Total:", producto_total)
    numero_actual = numero_actual + 1  
print("Todos los números del 1 al", limite, "es:", producto_total)
