import math

def lasku(Hsentti, hinta):
    Hmetri = Hsentti / 100
    pinta_ala = math.pi * (Hmetri / 2) ** 2
    Y_hinta = hinta / pinta_ala
    return Y_hinta

halkaisija1 = float(input("Ensimmäisen pizzan halkaisija : "))
euro1 = float(input("Ensimmäisen pizzan hinta : "))
halkaisija2 = float(input("Toisen pizzan halkaisija : "))
euro2 = float(input("Toisen pizzan hinta : "))
Yhinta1 = lasku(halkaisija1, euro1)
Yhinta2 = lasku(halkaisija2, euro2)

if Yhinta1 < Yhinta2:
    print("Ensimmäinen pizza on parempi vaihtoehto.")
elif Yhinta1 > Yhinta2:
    print("Toinen pizza on parempi vaihtoehto")
else:
    print("Kummatkin ovat saman arvoisia")

