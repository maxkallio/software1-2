def GetLitr(galon):
    litr = galon * 3.785
    return litr

while True:
    galon = int(input("Syöttäkää galloonien määrä: "))
    if galon < 0:
        break
    else:
        litr = GetLitr(galon)
        print(litr)