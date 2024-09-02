from random import random, randint


import random
nopat = int(input("Anna noppien määrä: "))
tulos = 0

for i in range(nopat):
    heitto = random.randint(1, 6)

    tulos += heitto

print(f"Silmälukujen summa on: {tulos}")
