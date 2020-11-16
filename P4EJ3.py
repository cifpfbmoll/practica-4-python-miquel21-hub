#PRÁCTICA 4 EJERCICIO 3
#Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos
#según que caso y muestre el resultado.

print("Calculadora de areas")
a=(input("Escribe c para cuadrado o t para triangulo\n"))
if (a=="c"):
    print("eres el cuadrado")
    base=int(input("Ponme la base"))
    altura=int(input("Ponme la altura"))
    print("El area del cuadrado es", (base*altura))
elif (a=="t"):
     print("soy el triángulo")
     base=int(input("Ponme la base"))
     altura=int(input("Ponme la altura"))
     print("El área del triangulo es", (base*altura)/2)
else :
     print("REPEAT")
