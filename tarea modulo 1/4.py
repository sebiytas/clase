palabra = input("dime una palabra ").lower()

while palabra == "":
    print("error. entrada no valida")
    palabra = input("dime una palabra ").lower()

for a, v in enumerate(palabra):
    a += 1
    if (v == "a" or v == "e") or (v == "i" or (v == "o" or v == "u")):
        multi = a * 3
        print(f"{v} - {multi}")

    else:
        divi = a // 2
        print(f"{v} - {divi}")

