luvut = []

while True:
    luku = input("Anna luku tai lopeta painamalla Enter: ")
    if luku == "":
        break
    luvut.append(int(luku))

luvut.sort(reverse=True)
print("Suurimmat numerot ovat: ")
for numero in luvut [:5]:
        print(numero)
