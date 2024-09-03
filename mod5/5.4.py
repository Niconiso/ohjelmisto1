kaupungit = []

for city in range(5):
    kaupunki = input("Anna kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("Viimeiset viisi syötettyä kaupunkia ovat: ")
for kaupunki in kaupungit:
    print(kaupunki)
