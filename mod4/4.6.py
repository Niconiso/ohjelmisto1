import random

pisteet = int(input("Anna arvottavien pisteiden määrä: "))
ympyränS = 0
i = 0

while i < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        ympyränS += 1
    i += 1

PiLiki = 4 * ympyränS / pisteet
print(f"Piin likiarvo on : {PiLiki}")
