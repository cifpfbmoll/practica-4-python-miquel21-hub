#PRÁCTICA 4 EJERCICIO 2
#Pida al usuario 5 números y diga si estos estaban en orden decreciente, / 	
# creciente o desordenados.
a=int(input("Introducir 1º dígito"))
b=int(input("Introducir 2º dígito"))
c=int(input("Introducir 3º dígito"))
d=int(input("Introducir 4º dígito"))
e=int(input("Introducir 5º dígito"))
if (a<b and b<c and c<d and d<e):
     print("Orden creciente")
elif (a>b and b>c and c>d and d>e):
     print ("Orden decreciente")
else :
     print("Orden desordenado")

