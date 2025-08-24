n = float(input("Ingrese una nota para dictaminar el rango: "))

if n < 0 or n > 5:
    print("dato invalido")
else:
    if n >= 4.6:
        print("Sobresaliente")
    elif n >= 4:
        print("Alto")
    elif n >= 3:
        print("Basico")
    else:
        print("Bajo")
    
    