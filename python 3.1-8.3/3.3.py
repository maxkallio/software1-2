# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.


arvo = (input("Anna sukupuolesi: nainen tai mies: "))

hemoglobiini = 0;

if arvo == "nainen":
    hemoglobiini = int(input("Anna naiseen hemoglobiini määrä g/l:ssa: "))
    if hemoglobiini < 117:
        print("naisen hemoglobiinimäärä on alhainen")
    elif hemoglobiini > 175:
        print("naisen hemoglobiinimäärä on korkea")
    elif hemoglobiini >= 117 and hemoglobiini <= 175:
        print("naisen hemoglobiinimäärä on normaali")

if arvo == "mies":
    hemoglobiini2 = int(input("Anna miehen hemoglobiini määrä g/l:ssa: "))
    if hemoglobiini2 < 134:
        print("miehen hemoglobiinimäärä on alhainen")
    elif hemoglobiini2 > 195:
        print("miehen hemoglobiinimäärä on korkea")
    elif hemoglobiini2 >= 134 and hemoglobiini2 <= 195:
        print("miehen hemoglobiinimäärä on normaali")