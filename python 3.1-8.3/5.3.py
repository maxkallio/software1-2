luku = 9

alkuluku = False

if luku == 1 or luku == 2:
    alkuluku = True
else:
    for i in range(2, luku, 1):
        print(i)
        if luku % i == 0:
            break
        alkuluku = True

if alkuluku:
    print(f'{luku} on alkuluku')
else:
    print(f'{luku} ei ole alkuluku')