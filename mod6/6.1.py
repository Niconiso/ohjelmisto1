import random

def noppa():
    return random.randint(1, 6)

def nopanheitto():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = noppa()
        print(f"Nopan määrä on: {silmaluku}")
nopanheitto()
