import random
a = int(input("How many dice to roll?  "))
sm = 0
for number_roll in range(1, a , 1):
    number = random.randint(1,6)
    sm += number
print(" sum of the numbers", sm)

