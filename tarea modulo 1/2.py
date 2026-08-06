secreto=24
respuesta= "si"

while respuesta == "si" :  
    for i in range(0, 3):
        respuesta= int(input(f"adivina el numero (tienes {3-i} intentos) "))
        if i <3:
            if respuesta < secreto:
                print("intento fallido. prueba con un numero mayor")
            
            elif respuesta >secreto:
                print("intento fallido. prueba con un numero menor")
            
            else:
                print(f"adivinaste, el numero es {secreto}")
                break           
    i +=1
    print("te quedaste sin intentos. PERDISTE")
respuesta = input("quiere volver a jugar? ")
    
            