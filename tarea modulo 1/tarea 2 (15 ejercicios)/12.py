dia = int(input("dime un dia "))
mes = int(input("dime un mes (del 1 al 12) "))
año = int(input("dime un año "))


if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    año_bisiesto = True
    if mes < 1 or mes > 12:
        print("error. datos invalidos")
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dias_max = 31
            if 1 <= dia <= dias_max:
                print(f"La fecha {dia}/{mes}/{año} es válida")
            else:
                print(f"Fecha inválida: El mes {mes} no tiene {dia} días (máximo {dias_max}).")
    elif mes in [4, 6, 9, 11]:
        dias_max = 30
    elif mes == 2:
        if año_bisiesto:
            dias_max = 29
        else:
            dias_max = 28
            
    
else:
    print("error. datos invalidos")

