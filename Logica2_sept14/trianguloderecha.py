n = 16
for puerta in range (1, n+1):
    espacios = ""
    signos = ""
    for e in range (n-puerta):
        espacios = espacios + " "
    for s in range (puerta):
        signos = signos + "#"
    print (espacios + signos)