import random

def noppa(tahkot):
    return random.randint(1, tahkot)

def nopanheitto():
    tahkot = int(input("Anna nopan tahkojen määrä: "))
    silmaluku = 0
    while silmaluku != tahkot:
        silmaluku = noppa(tahkot)
        print(f"Heitetty silmäluku: {silmaluku}")
nopanheitto()