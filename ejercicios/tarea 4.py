nro1 = int(input("dime un numero "))
nro2 = int(input("ahora dime otro numero "))

simbolo = input("ahora dime uno de estos cuatro simbolos para realizar un operacion matematica (+,*,-,/) ")

if simbolo == "+":
    suma = nro1 + nro2
    print(f"la suma de {nro1} y {nro2} da {suma}")
elif simbolo == "-":
    resta = nro1 - nro2
    print(f"la resta de {nro1} y {nro2} da {resta}")
elif simbolo == "/":
    div = nro1 / nro2
    print(f"la division de {nro1} entre {nro2} da como resultado {div}")
elif simbolo == "*":
    multi = nro1 * nro2
    print(f"la multiplicación de {nro1} con {nro2} da {multi}")
else:
    print("ese no es un simbolo valido")