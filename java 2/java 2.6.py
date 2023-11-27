import random

def roll_dice():
    return random.randint(1, 6)


print("<ul>")
while True:
    result = roll_dice()
    print(f"  <li>{result}</li>")
    if result == 6:
        break
print("</ul>")