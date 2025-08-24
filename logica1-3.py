nombre = input ("como te llamas: ")
edad = int(input("que edad tienes: "))
altura =float(input("cuanto mides: "))

presentacion =f"decilo, {nombre}"

es_adulto = edad >= 18 #booleano

print(presentacion)
print(f"Edad: {edad}años")
print(f"altura: {altura:.2f} metros ")
print("es adulto?:", es_adulto)