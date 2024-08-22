Kpituus = float(input("Ilmoita kuhan pituus sentteinä: "))
Kminimi = 37
if Kpituus < Kminimi:
    Kpituusero = Kminimi - Kpituus
    print(f"Kuha on liian {Kpituusero} senttiä liian pieni.")
else:
    print("Voit pitää kuhan.")
