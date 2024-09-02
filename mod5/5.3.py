alkuL = int(input("Anna luku, ja katsotaan onko se alkuluku: "))
if alkuL > 1:
    for i in range(2, (alkuL // 2) + 1):
        if (alkuL % i) == 0:
            print(f"Luku {alkuL} ei ole alkuluku")
            break
    else:
        print(f"{alkuL} on alkuluku")
else:
    print(f"{alkuL} ei ole alkuluku")