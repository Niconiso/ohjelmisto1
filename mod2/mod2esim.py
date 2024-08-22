# Syötteen lukeminen ja sijoittaminen muuttujaan
name = input("Anna nimesi: ")
# name = "Matti" # merkkijono (string)
# \ on espace-merkki, jolla voi tuottaa esim. tabin tai rivinvaihto
print("Moi \t " + name)

age = 7
print("Ikäsi on " + age)

age = int(age) + 1
age_string = str(age) # muutetaan int -> string, esim 8 -> "8"
print("Ikäsi on vuoden päästä " + age_string)
age = age + 1
print("Ikäsi on kahden vuoden päästä " + str(age))

height = float(input("Anna pituus: "))
#kasvatetaan 10cm
height = height + 0.1
#height = 1.8
print(f"Nimi: {name}, Ikä: {age}, Pituus: {height}")
