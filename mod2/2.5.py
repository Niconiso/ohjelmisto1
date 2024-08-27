leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

leivi_g = 20 * 32 * 13.3
naula_g = 32 * 13.3
luoti_g = 13.3

grammaTot = (leiviskat * leivi_g) + (naulat * naula_g) + (luodit * luoti_g)

kilogrammat = float(grammaTot // 1000)
grammat = grammaTot % 1000

print(f"Paino on {kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")