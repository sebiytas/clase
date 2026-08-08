consumo = int(input("ingrese el consumo de energia en KWh "))


if consumo <= 100:
    print("el monto a pagar es de 0.50$ por hora")
elif consumo > 100 and consumo <=300:
    print("el monto a pagar es de 1.00$ por hora")
elif consumo > 300:
    print("el monto a pagar es de 1.50$ por hora")
else:
    print("error. cantidad no valida")

