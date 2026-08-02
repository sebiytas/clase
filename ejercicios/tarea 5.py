compra = float(input("bienvenido, ingrese el monto total de su compra y recuerde q las compras de mas de 500$ tiene un 30% de descuento "))

if compra >= 500:
    descuento = compra * 0.30
    total = compra - descuento
    print(f"el precio resultante del descuento de su compra es {total}$")
else:
    print(f"su compra no tiene descuento. El monto total a pagar es {compra}")