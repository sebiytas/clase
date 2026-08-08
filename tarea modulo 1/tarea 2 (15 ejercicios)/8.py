lim = int(input("cual es el limite de velocidad? "))
vel = int(input("cual es la vel actual? "))
multa = 50

if vel > lim:
    exceso = vel - lim
    multa = 50 + (exceso * 5)
    print(f"superaste el limite de vel. tu multa es de {multa}")
elif vel <= lim:
    print("velocidad permitida sin multa por exceso de velocidad")
else:
    print("error. datos no validos")