import random

numero = random.randint(1, 10)

while True:

    lukuarvaus = int(input("Arvaa valitsemani luku: "))

    if lukuarvaus < numero:
        print("Liian pieni arvaus")
    elif lukuarvaus > numero:
        print("Liian suuri arvaus")
    elif lukuarvaus == numero:
        print("Oikein")