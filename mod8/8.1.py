import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1', #localhost, oma pc
         port= 3306,
         database='flight_game',
         user='root',
         password='31415926',
         autocommit=True
         )
def fetch_airport_by_icao(code):
    sql = f"select name, municipality from airport where ident='{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    return result_row

user_input = input("Syötä ICAO-koodi:")
airport = fetch_airport_by_icao(user_input)
#jos airport muuttujassa on jotain muuta kuin none/false/0
if airport:
    print(f"Lentokenttä on: {airport[0]}, {airport[1]}")
else:
    print("Lenttokenttää ei löydetty")

def add_airport(icao, name, municipality):
    sql = (f"INSERT INTO airport (id, ident, name, municipality) "
           f"VALUES (999, '{icao}', '{name}', '{municipality}');")
    cursor = connection.cursor()
    cursor.execute(sql)
icao = input("Anna uusi ICAO:")
name = input("Anna uuden kentän nimi: ")
municipality = input("Ja paikkakunta: ")
add_airport(icao, name, municipality)