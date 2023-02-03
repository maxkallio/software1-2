import mysql.connector


def haelentokentta(valinta):
    kursori = yhteys.cursor()
    query = "SELECT ident, name FROM airport WHERE ident 'like '" + str(valinta) + "'"
    kursori.execute(query)
    tulos = kursori.fetchall()
    print(tulos)
    if tulos:
        print("Lentokentän nimi: ", tulos)
        print("Kaupunki: ", tulos[1])
    else:
        print("Ei löydy..")
    yhteys.close()


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=8888,
         database='lento_peli',
         user='root',
         password='sala',
         autocommit=True
         )
