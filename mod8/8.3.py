import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='31415926',
         autocommit=True
         )

icao1 = input("Anna ensimmäinen ICAO-koodi: ")
icao2 = input("Anna toinen ICAO-koodi: ")

cursor = connection.cursor()
sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor.execute(sql, (icao1,))
kordinaatti1 = cursor.fetchone()
if kordinaatti1:
    kordinaatti1 = (kordinaatti1[0], kordinaatti1[1])

cursor.execute(sql, (icao2,))
kordinaatti2 = cursor.fetchone()
if kordinaatti2:
    kordinaatti2 = (kordinaatti2[0], kordinaatti2[1])

etäisyys = geodesic(kordinaatti1, kordinaatti2).kilometers
print(f"{icao1} ja {icao2} välinen etäisyys on {etäisyys} KM.")