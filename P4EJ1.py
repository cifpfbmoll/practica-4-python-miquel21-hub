#Práctica 4
#Ejercicio 1
#Pida al usuario 5 números y diga cuál es el mayor y cuál el menor.
a=float(input("Primer numero"))
b=float(input("Segundo numero"))
c=float(input("Tercer numero"))
d=float(input("Cuarto numero"))
e=float(input("Quinto numero"))
if (a<b and a<c and a<d and a<e):
    print("El", a, "es el menor")
elif (a>b and a>c and a>d and a>e):
    print("El", a, "es el mayor")
if (b<a and b<c and b<d and b<e):
    print("El", b, "es el menor")
elif (b>a and b>c and b>d and b>c):
    print("El", b, "es el mayor")
if (c<a and c<b and c<d and c<e):
    print("El", c, "es el menor")
elif (c>a and c>b and c>d and c>e):
    print("El", c, "es el mayor")
if (d<a and d<b and d<c and d<e):
    print("El", d, "es el menor")
elif (d>a and d>b and d>c and d>e):
    print("El", d, "es el mayor")
if (e<a and e<b and e<c and e<d):
    print("El", e, "es el menor")
elif (e>a and e>b and e>c and e>d):
    print("El", e, "es el mayor")
    


