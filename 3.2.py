#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.

#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.

#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

luokka = str(input("Valitse laivan hyttiluokka (LUX, A, B, C): "))

LUX = "LUX" or "lux"

A = "A" or "a"

B = "B" or "b"

C = "C" or "c"

if luokka == LUX:
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == A:
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == B:
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == C:
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka")
