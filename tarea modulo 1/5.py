plata = 5000

print("menu del banco ******")

acceder = input("desea acceder al banco? ").lower()

while acceder == "si":
    print("ingrese la accion que desea realizar")
    bank = input("1)Consultar 2)Retirar 3)salir ").lower()

    if bank == "consultar":
        print(f"su saldo es de {plata}")
    
    elif bank == "retirar":
        cuanto = int(input("cuantos billetes de 100 desea retirar? "))
        for i in range(1,cuanto+1):
            print("has retirado 100$ de tu cuenta")
            plata -=100

    
    elif bank == "salir":
        print("saliendo del banco")
        acceder = "no"
    
    else:
        print("error, entrada no valida")

