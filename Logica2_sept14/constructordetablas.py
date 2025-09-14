while True:
    print("\n1) ver tabla de multiplicar NxM")
    print ("0) Salir")
    op = input("opcion: ").strip()
    if op == "0":
        print ("suerte loka.")
        break
    elif op == "1":
        n = int(input("ingrese las filas (n)"))
        m = int(input("ingrese las filas (m)"))
        for i in range (1, n+1):
            for j in range (1, m+1):
                print(i*j, end ="\t")
            print()
    else:
        print("invalida")