#rectangulo de asteriscos que le vamos a pasar ancho por alto

alto = int(input("ingrese el valor del alto: "))
ancho = int(input("ingrese el valor del ancho: "))

for iguana in range(alto):
    fila = ""
    for mariguana in range (ancho):
        fila = fila + "*"
    print (fila)