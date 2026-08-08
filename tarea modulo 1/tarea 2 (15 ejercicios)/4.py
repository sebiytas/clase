entrada = 10
print("las entradas tiene un valor de 10$")

edad = int(input("antes de pagar ingrese su edad "))

if edad >= 60:
    descuento = entrada * 0.20
    total = entrada - descuento

    print(f"su monto total al pagar es de {total}$")
else:
    print(f"su monto total al pagar es de {entrada}$")
