import mysql.connector
from geopy.distance import geodesic as GD


def request(a):
    kursori = server.cursor()
    kursori.execute(a)
    tulos = kursori.fetchall()
    return tulos


server = mysql.connector.connect(
         host='127.0.0.1',
         port='3306',
         database='db1',
         user='root',
         password='1234',
         autocommit=True
         )

ident = [input("input first airport code"), input("input second airpot code")]
result = list()
for item in ident:
       result.append(request("SELECT latitude_deg, longitude_deg from airports where ident like '"+str(item)+"';"))
print(f"{GD(result[0][0],result[1][0]).km} km")
server.close()
