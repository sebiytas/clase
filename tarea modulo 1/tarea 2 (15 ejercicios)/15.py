print("dame 3 numeros")
num1 = int(input("nro 1 "))
num2 = int(input("nro 2 "))
num3 = int(input("nro 3 "))

if (num1 > num2 and num1 > num3) and (num2 > num3):
    print(f"los numeros se organizan de la siguiente manera: {num1}, {num2} y {num3}")
elif (num2 > num3 and num2 > num1) and (num1 > num3):
    print(f"los numeros se organizan de la siguiente manera: {num2}, {num1} y {num3}")
elif (num3 > num2 and num3 > num1) and (num1 > num2):
    print(f"los numeros se organizan de la siguiente manera: {num3}, {num1} y {num2}")
elif (num1 > num2 and num1 > num3) and (num2 < num3):
    print(f"los numeros se organizan de la siguiente manera: {num1}, {num3} y {num2}")
elif (num2 > num1 and num2 > num3) and (num3 > num1):
    print(f"los numeros se organizan de la siguiente manera: {num2}, {num3} y {num1}")
elif (num3 > num2 and num3 > num1) and (num2 > num1):
    print(f"los numeros se organizan de la siguiente manera: {num3}, {num2} y {num1}")
else:
    print("error. intente de nuevo")

