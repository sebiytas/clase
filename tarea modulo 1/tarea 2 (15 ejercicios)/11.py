salario = int(input("ingrese su salario "))

if salario <= 10000:
    print(f"el total a pagar es {salario}")
elif salario > 10000 and salario <= 30000:
    porcen = salario * 0.10
    total = salario + porcen
    print(f"el total a pagar es {total}")
elif salario > 30000:
    porcen = salario * 0.30
    total = salario + porcen
    print(f"el total a pagar es {total}")
else:
    print("error. datos no validos ")