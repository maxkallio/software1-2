num_participants = int(input("Enter the number of participants: "))
participants = []

for i in range(num_participants):
    name = input(f"Enter the name of participant {i + 1}: ")
    participants.append(name)

participants.sort()

print("Participants in alphabetical order:")
print("<ol>")
for participant in participants:
    print(f"  <li>{participant}</li>")
print("</ol>")