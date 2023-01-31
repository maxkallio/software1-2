# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.


kuukaudet = (
"tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu",
"marraskuu", "joulukuu")

talvi = ("joulukuu", "tammikuu", "helmikuu")
kevät = ("maaliskuu", "huhtikuu", "toukokuu")
kesä = ("kesäkuu", "heinäkuu", "elokuu")
syksy = ("syyskuu", "lokakuu", "marraskuu")

järjestysnumero = int(input("Anna kuukauden numerot (1-12): "))

if järjestysnumero == 12 or järjestysnumero == 1 or järjestysnumero == 2:
    kuukausi = kuukaudet[järjestysnumero - 1]
    print(f"{kuukausi} on {talvi.index(kuukausi) + 1} kuukausi talvella")

elif järjestysnumero == 3 or järjestysnumero == 4 or järjestysnumero == 5:
    kuukausi = kuukaudet[järjestysnumero - 1]
    print(f"{kuukausi} on {kevät.index(kuukausi) + 1} kuukausi kevällä")

elif järjestysnumero == 6 or järjestysnumero == 7 or järjestysnumero == 8:
    kuukausi = kuukaudet[järjestysnumero - 1]
    print(f"{kuukausi} on {kesä.index(kuukausi) + 1} kuukausi kesällä")

elif järjestysnumero == 9 or järjestysnumero == 10 or järjestysnumero == 11:
    kuukausi = kuukaudet[järjestysnumero - 1]
    print(f"{kuukausi} on {syksy.index(kuukausi) + 1} kuukausi syksyllä")

else:
    print("Sijoita oikein kuukausinumero")