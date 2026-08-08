print("vamos a evaluar triangulos")
lado1 = float(input("dime la medida del primer lado "))
lado2 = float(input("dime la medida del segundo lado "))
lado3 = float(input("dime la medida del tercer lado "))

if lado1 == lado2 and lado2 == lado3:
    print("el triangulo es equilatero")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("el triangulo es escaleno")
else:
    print("el triangulo es isosceles")