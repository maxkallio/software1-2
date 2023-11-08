list_1 = [2, 7, 16, 17]


def Summ(list):
    for num in list:
        if num % 2 != 0:
            list.remove(num)

    return list


print(list_1)
list_2 = Summ(list_1)
print(list_2)