letra = input("dime una letra del abecedario ").lower()

if (((letra == "a") or ((letra == "e") or (letra == "i")))  or ((letra == "o") or (letra == "u"))):
    print("tu letra es una vocal")
else:
    print("tu letra es una consonante")