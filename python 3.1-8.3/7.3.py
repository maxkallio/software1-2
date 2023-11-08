# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

icao = {"EFHK": "Helsinki-Vantaa"}

while True:
    quest = input("Mitä sinä haluat tehdä ? syötä, hae tai painaa 'Enter' jos haluat lopettaa: ")
    if quest == "syötä":
        print("ICAO-Koodi ja lentoasema sen jälkeen")
        icao_code = input("Syötä ICAO-koodin: ")
        lentoasema = input("Syötä lentoasema: ")
        icao[icao_code] = lentoasema

    while quest == "hae":
        quest = input("Sijoita ICAO koodi tai paina 'Enter' jos haluat lopettaa: ")
        if quest in icao:
            print(f"{quest} ICAO koodi on {icao[quest]} lentoasema")
        else:
            print("Väärin ICAO koodi, tai koodi ei ole datassa")
            break

    if quest == "":
        break

print("Moikka!")
