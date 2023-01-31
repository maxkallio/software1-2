# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()

while True:
    inputti = input("Enter a name: ")
    if inputti == "":
        break
    elif inputti in nimet:
        print("Tämän nimi on jo listilla ")
    else:
        nimet.add(inputti)
        print("Nimi on lisäntynyt")

for item in nimet:
    print(item)