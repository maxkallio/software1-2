import random
from geopy.distance import geodesic
from yhteys import yhteys

def LuoPeli(pNimi, polttoAine, omatSotilaat, raha):
    sql = "INSERT INTO Game(Fuel, Money, Troops, User_name) VALUES('" + str(polttoAine) + "', '" + str(raha) + "', '" + str(omatSotilaat) + "', '" + pNimi + "')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    global PeliID
    sql2 = "SELECT MAX(Game_ID) FROM Game WHERE User_name = '" + pNimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql2)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            PeliID = rivi[0]
    return
def ArvoPaikat():
    sql = "SELECT iso_country FROM airport WHERE continent = 'EU' GROUP BY iso_country ORDER BY RAND() LIMIT 3"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            sql2 = "SELECT ident, name FROM airport WHERE iso_country = '" + rivi[0] + "' ORDER BY RAND() LIMIT 1"
            kursori.execute(sql2)
            tulos2 = kursori.fetchall()
            if kursori.rowcount > 0:
                for rivi2 in tulos2:
                    paikka = [rivi2[0], rivi2[1], rivi[0], "Ei valloitettu"]
                    paikat.append(paikka)
    ValitseAloitus(paikat)
    return

def LuoSotilaat(lista):
    for i in range(len(lista)):
        valiVaihe = lista[i]
        if valiVaihe[3] != "Valloitettu":
            noppa = random.randint(1, 3)
            maara = 0
            if noppa == 1:
                maara = 500
            elif noppa == 2:
                maara = 750
            elif noppa == 3:
                maara = 1000
            sql = "INSERT INTO Troops(Airport_ID, Count, Visited) VALUES('" + valiVaihe[0] + "', '" + str(maara) + "', 0)"
            kursori = yhteys.cursor()
            kursori.execute(sql)
    return

def GetLentokentanSotilaat(ident):
    sql = "SELECT Count FROM Troops WHERE Airport_ID = '" + ident + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            return rivi[0]
    return

def SetLentokentanSotilaat(ident, maara):
    sql = "UPDATE Troops SET Count = '" + str(maara) + "' WHERE Airport_ID = '" + ident + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def Taistelu(ident):
    omat = float(GetSotilaat())
    viholliset = float(GetLentokentanSotilaat(ident))
    if omat > 0:
        while True:
            print("Taistelu meneilllään. Omat sotilaat: " + str(omat) + ", vihollisen sotilaat: " + str(viholliset))
            omaHyokkays = random.randint(int(0.01 * omat), int(0.1 * omat))
            vihollisenHyokkays = random.randint(int(0.01 * viholliset), int(0.1 * viholliset))

            if omaHyokkays < 1:
                omaHyokkays = 1

            if vihollisenHyokkays < 1:
                vihollisenHyokkays = 1

            #print("Omien hyökkäys: " + str(omaHyokkays) + ", vihollisen hyökkäys: " + str(vihollisenHyokkays))
            omat -= vihollisenHyokkays
            viholliset -= omaHyokkays

            if omat <= 0:
                omat = 0
                print("Hävisit taistelun.")
                if viholliset <= 0:
                    viholliset = 0
                SetSotilaat(omat)
                SetLentokentanSotilaat(ident, viholliset)
                return False
            if viholliset <= 0:
                viholliset = 0
                SetLentokentanSotilaat(ident, viholliset)
                if omat > 0:
                    print("Voitit taistelun.")
                    SetSotilaat(omat)
                    return True
        return
    else:
        print("Tarvitset sotilaita vallataksesi lentoaseman.")
        return False

def Valloita(ident):
    global paikat
    for i in range(len(paikat)):
        valiVaihe = paikat[i]
        if ident == valiVaihe[0]:
            valiVaihe[3] = "Valloitettu"
    return

def GetValloitus(ident):
    global paikat
    for i in range(len(paikat)):
        valiVaihe = paikat[i]
        if ident == valiVaihe[0]:
            return valiVaihe[3]
    return

def ValitseAloitus(lista):
    global nykySijainti
    asemat = "Valitse aloitusasema kirjoittamalla lentokentän icao-koodi:\n"
    for i in range(len(lista)):
        valiVaihe = lista[i]
        asemat += "Icao-koodi: " + valiVaihe[0] + ", nimi: " + valiVaihe[1] + ", maa: " + valiVaihe[2] + "\n"
    '''
    Tallenna tietokantaan muutokset
    '''
    print(asemat)
    aloitusAsema = input("Aloitusasema: ")
    nykySijainti = aloitusAsema
    Valloita(nykySijainti)
    return

def GetRaha():
    sql = "SELECT Money FROM Game WHERE Game_ID = '" + str(PeliID) + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            return str(rivi[0])
    return

def GetPolttoAine():
    sql = "SELECT Fuel FROM Game WHERE Game_ID = '" + str(PeliID) + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            return str(rivi[0])
    return

def GetSotilaat():
    sql = "SELECT Troops FROM Game WHERE Game_ID = '" + str(PeliID) + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            return str(rivi[0])
    return

def SetRaha(raha):
    sql = "UPDATE Game SET Money = '" + str(raha) + "' WHERE Game_ID = '" + str(
        PeliID) + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def SetPolttoAine(polttoAine):
    sql = "UPDATE Game SET Fuel = '" + str(polttoAine) + "' WHERE Game_ID = '" + str(
        PeliID) + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def SetSotilaat(sotilaat):
    sql = "UPDATE Game SET Troops = '" + str(sotilaat) + "' WHERE Game_ID = '" + str(
        PeliID) + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
def Haekoordinaatit(ident):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + ident + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            return str(rivi[0]) + ", " + str(rivi[1])
    return
def Matkat(lista):
    matkat = "Valitse matka kirjoittamalla lentokentän icao-koodi:\n"
    tyhja = True
    polttoAine = float(GetPolttoAine())
    for i in range(len(lista)):
        valiVaihe = lista[i]
        etaisyys = geodesic(Haekoordinaatit(nykySijainti), Haekoordinaatit(valiVaihe[0])).km
        if valiVaihe[0] != nykySijainti:
            if etaisyys <= float(polttoAine) and valiVaihe[3] != "Valloitettu":
                tyhja = False
                matkat += "Icao-koodi: " + valiVaihe[0] + ", nimi: " + valiVaihe[1] + ", maa: " + valiVaihe[2]\
                      + ", matka: " + str(etaisyys) + ", " + valiVaihe[3] + ", sotilaat: " + str(GetLentokentanSotilaat(valiVaihe[0])) + "\n"
    if tyhja == True:
        return print("Et voi matkustaa mihinkään.")
    else:
        print(matkat)
        kohde = input("Matkustuskohde: ")
        Matkusta(kohde)
        return
    return

def Matkusta(kohde):
    global nykySijainti
    polttoAine = float(GetPolttoAine())
    etaisyys = geodesic(Haekoordinaatit(nykySijainti), Haekoordinaatit(kohde)).km
    if etaisyys <= polttoAine and GetValloitus(kohde) != "Valloitettu":
        if Taistelu(kohde):
            polttoAine -= etaisyys
            nykySijainti = kohde
            SetPolttoAine(polttoAine)
            Valloita(nykySijainti)
            MatemaattinenOngelma()
    else:
        return print("Epäkelpo vastaus.")
    return

def MatemaattinenOngelma():
    sql = "SELECT Questions_text, Answer FROM Questions ORDER BY RAND() LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print("Vastaa seuraavaan kysymykseen oikein suorittaaksesi kidnappauksen: " + rivi[0])
            vastaus = input("Vastaus: ")
            if float(vastaus) == float(rivi[1]):
                print("Vastaus oikein. Sait kidnappauksesta 1000 €")
                raha = float(GetRaha()) + float(1000)
                SetRaha(raha)
            else:
                print("Vastaus väärin.")
    return

def HavinnytTarkistus(lista):
    global nykySijainti
    polttoAine = GetPolttoAine()
    raha = GetRaha()
    lahin = ""
    global havinnyt
    for i in range(len(lista)):
        valiVaihe = lista[i]
        if valiVaihe[0] != nykySijainti and valiVaihe[3] != "Valloitettu":
            if lahin == "":
                lahin = valiVaihe[0]
            elif geodesic(Haekoordinaatit(nykySijainti), Haekoordinaatit(lahin)).km > geodesic(
                    Haekoordinaatit(nykySijainti), Haekoordinaatit(valiVaihe[0])).km:
                lahin = valiVaihe[0]
    etaisyys = geodesic(Haekoordinaatit(nykySijainti), Haekoordinaatit(lahin)).km
    maxPolttoAine = float(polttoAine) + (float(raha) * 2)

    if float(raha) < 2 and int(GetSotilaat()) == 0:
        havinnyt = True
        return print("Hävisit pelin")
    elif etaisyys > maxPolttoAine:
        havinnyt = True
        return print("Hävisit pelin")
    return
def VoittoTarkistus(lista):
    voitto = True
    for i in range(len(lista)):
        valiVaihe = lista[i]
        if valiVaihe[3] == "Ei valloitettu":
            voitto = False
    return voitto

def Voitto():
    while True:
        valinta = input("Voitit pelin. Valitse seuraavista vaihtoehdoista mitä haluat tehdä valloittamallesi maailmalle:\n1) Rupea lentokenttien yksinvaltiaaksi\n"
                        "2) Anna lentokentät kansalaisille\nValinta: ")
        if valinta == "1":
            print("Rupesit lentokenttien yksinvaltiaaksi.")
            break
        elif valinta == "2":
            print("Annoit lentokentät kansalaisille.")
            break
        else:
            print("Syötä toimintoa vastaava numero.")
def LentokentanNimi(ident):
    sql = "SELECT name FROM airport WHERE ident = '" + ident + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            return str(rivi[0])
    return

def Kauppa():
    while True:
        print(f"Rahamäärä: {GetRaha()} €. Polttoainemäärä: {GetPolttoAine()} km. Sotilasmäärä: {GetSotilaat()}\n")
        valinta = input("Valitse toiminto kirjoittamalla toimintoa vastaava luku:\n"
                        "1) Osta polttoainetta\n2) Osta sotilaita\n3) Poistu kaupasta\nValinta: ")

        if valinta == "1":
            maara = float(input("Kuinka monta km haluat ostaa polttoainetta: "))
            OstaPolttoAinetta(maara)
        elif valinta == "2":
            maara = float(input("Kuinka monta sotilasta haluat ostaa: "))
            OstaSotilaita(maara)
        elif valinta == "3":
            break
        else:
            print("Epäkelpo luku. Yritä uudestaan.")

def Maksu(hinta, maara, tyyppi):
    polttoAine = float(GetPolttoAine())
    raha = float(GetRaha())
    omatSotilaat = float(GetSotilaat())
    if tyyppi == "polttoaine":
        valinta = input(f"Olet ostamassa polttoainetta {maara} km verran. Se tulee maksamaan {hinta} €.\n"
              f"Syötä '1' hyväksyäksesi ostoksen tai syötä '2' kumotaksesi ostoksen: ")
        if valinta == "1":
            if raha - hinta >= 0:
                raha -= hinta
                polttoAine += maara
                SetRaha(raha)
                SetPolttoAine(polttoAine)
                return print("Kiitos ostoksestasi")
            else:
                return print("Rahasi eivät riitä ostokseen.")
        elif valinta == "2":
            return print("Ostoksesi on peruutettu.")
    elif tyyppi == "sotilas":
        valinta = input(f"Olet ostamassa sotilaita {maara} verran. Se tulee maksamaan {hinta} €.\n"
                        f"Syötä '1' hyväksyäksesi ostoksen tai syötä '2' kumotaksesi ostoksen: ")
        if valinta == "1":
            if raha - hinta >= 0:
                raha -= hinta
                omatSotilaat += maara
                SetRaha(raha)
                SetSotilaat(omatSotilaat)
                return print("Kiitos ostoksestasi")
            else:
                return print("Rahasi eivät riitä ostokseen.")
        elif valinta == "2":
            return print("Ostoksesi on peruutettu.")

def OstaPolttoAinetta(maara):
    #2km = 1€
    Maksu(maara/2, maara, "polttoaine")

def OstaSotilaita(maara):
    #1s = 2€
    Maksu(maara * 2, maara, "sotilas")

pNimi = input("Anna pelaajanimi: ")
polttoAine = 1000
omatSotilaat = 1000
raha = 1000
paikat = []
nykySijainti = "" #tulee tietokannasta
PeliID = 0
havinnyt = False
LuoPeli(pNimi, polttoAine, omatSotilaat, raha)
ArvoPaikat()
LuoSotilaat(paikat)

while True:
    if VoittoTarkistus(paikat):
        Voitto()
        break

    HavinnytTarkistus(paikat)
    if havinnyt:
        break

    print("Pelaajanimi: " + pNimi +", sijainti: " + nykySijainti + ", lentokentän nimi: " + LentokentanNimi(nykySijainti)
          + ", polttoaine: " + GetPolttoAine() + " km, sotilaat: " + GetSotilaat() + ", raha: " + GetRaha() + " €")
    valinta = input("Valitse vaihtoehdoista kirjoittamalla sitä vastaava luku:\n1) Matkusta\n2) Mene kauppaan\n3) Lopeta peli\nValinta: ")
    if valinta == "1":
        Matkat(paikat)
    elif valinta == "2":
        Kauppa()
    elif valinta == "3":
        break