cantidad = int(input("dime una cantidad de numeros a evaluar "))
negativo = 0
positivo = 0
cero = 0
while cantidad <= 0:
    print("error, la cantidad no puede ser menor o igual a 0")
    cantidad = int(input("dime una cantidad de numeros a evaluar "))

for i in range(1,cantidad+1):
    eva = int(input(f"dime la cifra numero {i} "))
    if eva < 0:
            negativo += 1
    elif eva > 0:
            positivo += 1
    else:
            cero += 1
print(f"de entre las {cantidad} cifras que me diste hay {negativo} negativos y {positivo} positivos y {cero} ceros")
