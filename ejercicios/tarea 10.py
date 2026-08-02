nro1 = int(input("dame un numero para dividir "))
nro2 = int(input("ahora dame otro numero "))

if nro2 != 0:
    division = nro1 / nro2
    print(f"el resultado da {division}")
else:
    print("error, el 0 no se puede usar como divisor")