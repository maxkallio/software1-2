#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
#niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumat = float(input('Anna tummat: '))

while tuumat >= 0:
    print(f'{tuumat} tuuma on {2.54 * tuumat} senttiä ')
    tuumat = float(input('Anna tummat: '))