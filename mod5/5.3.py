alkuL = int(input("Anna tarkistettava luku: "))
if alkuL > 1:
    for i in range(2, (alkuL // 2) + 1):
        if (alkuL % i) == 0:
            print(f"Luku {alkuL} ei ole alkuluku")
            break
    else:
        print(f"{alkuL} on alkuluku")
if alkuL == 0:
    print(f"{alkuL} ei ole alkuluku")