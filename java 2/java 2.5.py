given_numbers = set()

while True:
    num = float(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    if num in given_numbers:
        print("Number already given. Stopping program.")
        break
    given_numbers.add(num)

all_numbers = list(given_numbers)
all_numbers.sort()

print("All given numbers in ascending order:")
for num in all_numbers:
    print(num)