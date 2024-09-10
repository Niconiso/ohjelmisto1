nimet = set()
while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Tämä on uusi nimi")
        nimet.add(nimi)

print("Syötetyt nimet:")
for nimi in nimet:
    print(nimi)
