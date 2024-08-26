Vuosi = int(input("Anna vuosiluku: "))
if Vuosi % 4 == 0:
    print(f"{Vuosi} on karkausvuosi")
elif Vuosi % 400 == 0:
    print(f"{Vuosi} on karkausvuosi")
else:
    print(f"{Vuosi} ei ole karkausvuosi")