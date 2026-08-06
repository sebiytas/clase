import random
jugar = "si"

while jugar == "si" :
    secreto = random.randint(1,10)
    for i in range(0, 3):
        respuesta= int(input(f"adivina el numero entre el 1 y el 10 (tienes {3-i} intentos) "))
        if i == 2:
            print("te quedaste sin intentos. PERDISTE") 
        elif i <3:
            if respuesta == secreto:
                print(f"adivinaste, el numero es {secreto}")
                break
            elif respuesta >secreto:
                print("intento fallido. prueba con un numero menor")           
            else: 
                print("intento fallido. prueba con un numero mayor")
        i +=1
        
    jugar = input("quiere volver a jugar? ").lower()
    
            