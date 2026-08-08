dia = int(input("Ingresa el día: "))
mes = int(input("Ingresa el mes (1-12): "))
anio = int(input("Ingresa el año: "))

es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

if mes < 1 or mes > 12 or anio < 1:
    print("Fecha inválida: El mes debe estar entre 1 y 12 y el año ser positivo.")
else:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias_maximos = 31
    elif mes in [4, 6, 9, 11]:
        dias_maximos = 30
    elif mes == 2:
        if es_bisiesto:
            dias_maximos = 29
        else:
            dias_maximos = 28

    if 1 <= dia <= dias_maximos:
        print(f"¡La fecha {dia}/{mes}/{anio} es válida!")
    else:
        print(f"Fecha inválida: El mes {mes} no tiene {dia} días (máximo {dias_maximos}).")
