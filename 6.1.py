import random

def GetNumber():
    num = random.randint(1, 6)
    print(num)
    return num

while True:
    num = GetNumber()
    if num == 6:
        break