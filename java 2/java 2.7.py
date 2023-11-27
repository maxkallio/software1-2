def roll_dice_with_sides(sides):
    return random.randint(1, sides)


max_number = int(input("Enter the maximum number on the dice: "))
print("<ul>")
while True:
    result = roll_dice_with_sides(max_number)
    print(f"  <li>{result}</li>")
    if result == max_number:
        break
print("</ul>")