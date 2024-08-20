def Kilogrammoina(leiviskat, naulat, luodit):
    leivi_g = 20 * 32 * 13.3
    naula_g = 32 * 13.3
    luoti_g = 13.3
    grammaT = (leiviskat * leivi_g) + (naulat * naula_g) + (luodit * luoti_g)

    kilogrammat = float(grammaT // 1000)
    grammat = grammaT % 1000
    return kilogrammat, grammat

def main():
    leiviskat = float(input("Anna leiviskät: "))
    naulat = float(input("Anna naulat: "))
    luodit = float(input("Anna luodit: "))

    kilogrammat, grammat = Kilogrammoina(leiviskat, naulat, luodit)
    print(f"Paino on {kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")

#Tämä alempi osa oli pakko katsoa netistä ohjeena, en ihan ymmärtänyt miksi ei pyörinyt ilman
if __name__ == "__main__":
    main()