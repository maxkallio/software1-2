list = (1, 7, 15, 57, 5)


def Summ(list):
    summ = 0
    for num in list:
        summ += num

    return summ


summ = Summ(list)
print(summ)