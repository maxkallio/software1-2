dogs = []

for i in range(6):
    dog_name = input("Enter a dog's name: ")
    dogs.append(dog_name)

dogs.sort(reverse=True)

print("Dog names in reverse alphabetical order:")
print("<ul>")
for dog in dogs:
    print(f"  <li>{dog}</li>")
print("</ul>")