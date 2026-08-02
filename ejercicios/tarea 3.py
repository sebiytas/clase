nro = int(input("dime un numero para determinar si es par o impar "))

resultado = nro % 2

if resultado == 0:
    print(f"{nro} es un numero par")
else:
    print(f"{nro} es un numero impar")