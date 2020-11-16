#PRÁCTICA 4 EJERCICIO 4
#Pida al usuario tres números y un cuarto número, y compruebe si este último \n
#es divisor de los tres números primeros.
print("Hola, estas en la calculadora comprobadora de divisores")
a=int(input("Inserte el primer número"))
b=int(input("Inserte el segundo número"))
c=int(input("Inserte el tercer número"))
d=int(input("Inserte el número divisor"))
if (a%d and b%d and c%d) == 0 :
     print("El número escogido es divisor")
else :
     print("El número escogido no es divisor")


 	
