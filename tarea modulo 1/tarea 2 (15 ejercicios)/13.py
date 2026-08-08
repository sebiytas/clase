jug1 = input("(jugador 1) juguemos piedra, papel o tijeras. escribe una de las opciones ").lower()
jug2 = input("(jugadr 2) juguemos piedra, papel o tijeras. escribe una de las opciones ").lower()

if jug1 == jug2:
    print("empate")
elif (jug1 == "piedra" and jug2 == "tijera") or (jug1 == "papel" and jug2 == "piedra"):
    print("jugador 1 gana")
elif (jug2 == "piedra" and jug1 == "tijera") or (jug2 == "papel" and jug1 == "piedra"):
    print("jugador 2 gana")
else:
    print("error.entradano valida")