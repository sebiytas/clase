saldo = 1000

print(f"tu saldo es de {saldo}")
retiro = int(input("ingresa un monto a retirar "))

if retiro % 10 == 0:
    saldo -= retiro
    print(f"retiro por {retiro}$ exitoso")
    print(f"tu saldo restante es {saldo}")
else:
    print("error. el monto a retirar debe ser multiplo de 10")