import random

def heitto():
    return random.randint(1, 6)

def lasku():
    while True:
        silmaluku = heitto()
        print(f"Nopasta tuli: {silmaluku}")
        if silmaluku == 6:
            break
lasku()
