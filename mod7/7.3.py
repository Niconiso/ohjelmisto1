lentoasemat = {}

while True:
    print("Valitse toiminto:")
    print("1. syötä uusi lentoasema")
    print("2. hae lentoaseman tiedot")
    print("3. lopeta")
    toiminto = input("anna valinta: ")

    if toiminto == "1":
        icao = input("anna lentoaseman ICAO-koodi: ")
        nimi = input("anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"lentoasema {nimi} ja ICAO {icao} lisätty.")

    elif toiminto == "2":
        icao = input("anna lentoaseman ICAO-koodi: ")
        if icao in lentoasemat:
            print(f"lentoasema: {lentoasemat[icao]}")

    elif toiminto == "3":
        break
