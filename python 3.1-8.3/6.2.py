import random

set_num = 21

def GetNumber(get_num):
    num = random.randint(1, get_num)
    print(num)
    return num

while True:
    num = GetNumber(set_num)
    if num == set_num:
        break