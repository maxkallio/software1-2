# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuos = int(input("Anna lukuvuosi: "))

if vuos % 4 == 0:
    print("Vuosi on karkaus")
else:
    print("Vuosi ei ole karkaus")
