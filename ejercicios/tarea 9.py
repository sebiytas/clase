##medidor de temp
temp = int(input("ingrese la temperatura del ambiente "))

if ((temp > 15) and (temp < 25)):
    print("estás en un ambiente templado")
elif temp <= 15:
    print("estás en un ambiente frio")
else:
    print("estás en un ambiente caluroso")