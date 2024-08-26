Bsukupuoli = input("Mikä on biologinen sukupuolesi (mies/nainen): ")
HemoG = float(input("Sekä hemoglobiiniarvosi (g/l): "))

if Bsukupuoli == "nainen":
    alhainen = 114
    korkea = 155

elif Bsukupuoli == "mies":
    alhainen = 134
    korkea = 167

if HemoG < alhainen:
    print("Hemoglobiiniarvosi on alhainen.")
elif (HemoG > korkea):
    print("Hemoglobiiniarvosi on korkea.")
else:
    print("Hemoglobiiniarvosi ovat normaalit.")