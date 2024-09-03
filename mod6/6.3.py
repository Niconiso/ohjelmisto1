def litra(gallona):
    return gallona * 3.785

def bensa():
    while True:
        gallona = float(input("Anna bensiinin määrä: "))
        if gallona < 0:
            break

        print(f"{gallona} gallonaa on {litra(gallona):.2f} litraa.")
bensa()