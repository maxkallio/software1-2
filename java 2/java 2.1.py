numbers = []

for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)

print("Numbers in reverse order:")
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])