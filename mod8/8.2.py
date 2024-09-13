import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1', #localhost, oma pc
         port= 3306,
         database='flight_game',
         user='root',
         password='31415926',
         autocommit=True
         )

cursor = connection.cursor()
maakoodi = input("Anna maakoodi: ")
sql = f"SELECT type, count(*) FROM airport WHERE iso_country = %s GROUP BY type;"
cursor.execute(sql,(maakoodi,))

tulokset = cursor.fetchall()
if tulokset:
    for type, count in tulokset:
        print(f"{type} {count} lentokenttää")
