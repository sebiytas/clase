cuenta = float(input("ingrese el total de su cuenta "))

respuesta = (input("quieres dejar un 15% de pronina? (si/no) ")).lower()

if respuesta == "si":

    propina = cuenta * 0.15

    total = cuenta + propina

    print(f"el monto total a pagar es de {total}$")

elif respuesta == "no":
    print(f"el monto total a pagar es de {cuenta}$")

else:
    print("error")