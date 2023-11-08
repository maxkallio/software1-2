#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).


print("Sijoita oikein käyttäjätunnus ja salasana ")

kertaa = 0
tunnus = ""
passw = ""

while kertaa < 5:
    tunnus = input("Sijoita tunnus: ")
    passw = input("Sijoita salasana: ")
    if passw == "rules" and tunnus == "python":
        print("Tervetuloa")
        break
    else:
        print("Tunnus tai salasana on väärin. Yrittää uudellen. ")
        kertaa += 1

while kertaa == 5:
    print("Pääsy on evätty")
    break