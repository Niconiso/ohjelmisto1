vuodenajat = (
    ("talvi", (12, 1, 2)),
    ("kevät", (3, 4, 5)),
    ("kesä", (6, 7, 8)),
    ("syksy", (9, 10, 11)))
kuukausi = int(input("Anna kuukauden numero : "))

vuodenaika = "ei ole kuukausi"
for vuosi, kuukaudet in vuodenajat:
    if kuukausi in kuukaudet:
        vuodenaika = vuosi
        break

print(f"{kuukausi} kuukausi on {vuodenaika}.")

