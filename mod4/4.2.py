tuuma = float(input("Anna tuumamäärä: "))
sentit = tuuma * 2.54
if tuuma > 1:
    print(f"{tuuma} tuumaa on {sentit} cm.")
elif tuuma < 1:
    print("Lopetetaan toiminta.")