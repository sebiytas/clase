promedio = int(input("ingrese su promedio "))
ingresos = int(input("ingrese el monto de sus ingresos "))
distancia = int(input("ingrese la distancia a la que se encuentra del instituto "))

if promedio > 90 and ingresos < 500:
    print("felicidades, te has gando la beca completa")
elif promedio > 80 and distancia > 50:
    print("felicidades, te has gando la beca transporte")
else:
    print("lo siento, pero no has obtenido niguna beca")

