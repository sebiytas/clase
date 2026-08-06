
numero = int(input("ingrese un numero entero positivo "))
suma = 0
while numero <=0:
    print("error, el numero debe ser positivo")
    numero = int(input("ingrese un numero entero positivo "))
    
for vacio in range(0, numero +1):
    if vacio % 2 == 0:
        suma += vacio
vacio += 1
print(f"la suma de todos los numeros pares desde el 0 hasta el {numero} da {suma}")





    