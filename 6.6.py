from cmath import pi


def cena_pizza(diameter,price):
    square= diameter * diameter / 4 * pi
    summa= price / square
    return summa

a = int(input("diameter of the first pizza "))
b = int(input("price of the first cena pizza "))
first = cena_pizza(a,b)

c = int(input("diameter of the second pizza "))
d = int(input("price of the second pizza "))
second = cena_pizza(c,d)

if(first < second):
    print("The first pizza is more profitable than the second")
elif(first > second):
    print("the second pizza is more profitable than the first")