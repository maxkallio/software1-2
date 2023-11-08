import mysql.connector

def request(a):
    kursori = server.cursor()
    kursori.execute(a)
    tulos = kursori.fetchall()
    server.close()
    return tulos


server = mysql.connector.connect(
         host='127.0.0.1',
         port='3306',
         database='db1',
         user='root',
         password='1234',
         autocommit=True
         )

country = input("type country code ")
q = "SELECT type from airports where iso_country like '"+str(country)+"';"
result = request(q)
balloonport_count = 0
closed_count = 0
heliport_count = 0
small_airport_count = 0
seaplane_base_count = 0
medium_airport_count = 0
large_airport_count = 0
airports = ['balloonport', 'closed', 'heliport', 'small_airport', 'seaplane_base', 'medium_airport', 'medium_airport']
airports_vars = [balloonport_count, closed_count, heliport_count, small_airport_count,  seaplane_base_count, medium_airport_count, large_airport_count]
for item in result:
    item = list(item)
    for i,name in enumerate(airports):
        if(item[0] == name):
            airports_vars[i] += 1
for i,name in enumerate(airports):
    print(f"{name}: {airports_vars[i]}")