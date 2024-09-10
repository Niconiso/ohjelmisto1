import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1', #localhost, oma pc
         port= 3306,
         database='flight_game',
         user='root',
         password='31415926',
         autocommit=True
         )
print(connection)

cursor = connection.cursor()
cursor.execute("SELECT continent, name, iso_country FROM country")
#result = cursor.fetchone() #fetchone hakee rivi kerrallaan
#print(result)
#result = cursor.fetchmany() #fetchmany hakee halutun määrän rivejä kerrallaan antamalla numerolla
#print(result)
result = cursor.fetchall() #fetchall palauttaa kaikki (loput) rivit listana
print(result)
#tuloslista käsitellään toistorakenteella
for row in result:
    print(f"{row[1]}, Maakoodi: {row[2]}, maanosa: {row[0]}")