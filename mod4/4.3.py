luvut = []

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luvut.append(float(luku))

if luvut:
    print(f"Pienin luku on: {min(luvut)}")
    print(f"Suurin luku on: {max(luvut)}")
