print("comparemos dos numeros")
nro1 = float(input("dime el primer numero "))
nro2 = float(input("dime el segundo numero "))

if nro1 == nro2:
    print(f"ambos numeros tienen el mismo valor ({nro1})")
elif nro1 < nro2:
    print(f"el {nro2} es el numero mayor y el {nro1} el menor")
else:
    print(f"el {nro1} es el numero mayor y el {nro2} el menor")