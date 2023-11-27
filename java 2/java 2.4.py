numbers = []

while True:
    num = float(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

numbers.sort(reverse=True)

print("Numbers in descending order:")
for num in numbers:
    print(num)