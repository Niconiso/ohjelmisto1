kokeilut = 0

while kokeilut < 5:
    Tunnus = input("Käyttäjätunnus: ")
    Salasana = input("Salasana: ")

    if Tunnus == "Python" and Salasana == "Rules":
        print("Tervetuloa")
        break
    else:
        print("Syötä tiedot uudelleen")
        kokeilut += 1
if kokeilut == 5:
    print("Pääsy evätty")

