#PRÁCTICA 4 EJERCICIO 5
#Pida al usuario un importe en euros y diga si el cajero automático le puede dar \n
#dicho importe utilizando el mismo billete y el más grande.	
extracción=int(input("Cuanto dinero desea extraer"))

if (extracción%500) == 0:
    Cuenta_Billetes = extracción/ 500
    print("El cajero le devuelve ", str(Cuenta_Billetes) + " billete/s de 500")
elif (extracción%200) == 0 :
    Cuenta_Billetes = extracción/ 200
    print("El cajero le devuelve",str(Cuenta_Billetes), "billete/s de 200")
elif (extracción%100) == 0 :
    Cuenta_Billetes = extracción/ 100
    print("El cajero le devuelve", str(Cuenta_Billetes), "billete/s de 100")
elif (extracción%50) == 0 :
    Cuenta_Billetes = extracción/ 50
    print("El cajero le devuelve", str(Cuenta_Billetes), "billete/s de 50")
elif (extracción%20) == 0 :
    Cuenta_Billetes = extracción/ 20
    print("El cajero le devuelve", str(Cuenta_Billetes), "billete/s de 20")
elif (extracción%10) == 0 :
    Cuenta_Billetes = extracción/ 10
    print("El cajero le devuelve", str(Cuenta_Billetes),  "billete/s de 10")
elif (extracción%5) == 0 :
    Cuenta_Billetes= extracción/ 5
    print("El cajero le devuelve", str(Cuenta_Billetes), "billete/s de 5")