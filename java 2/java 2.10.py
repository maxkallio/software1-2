num_candidates = int(input("Enter the number of candidates: "))
candidates = []


for i in range(num_candidates):
    name = input(f"Name for candidate {i + 1}: ")
    candidates.append({"name": name, "votes": 0})

num_voters = int(input("Enter the number of voters: "))


for i in range(num_voters):
    vote = input(f"Voter {i + 1}, enter the name of the candidate you will vote for (or press Enter for an empty vote): ")
    for candidate in candidates:
        if candidate["name"] == vote:
            candidate["votes"] += 1
            break


candidates.sort(key=lambda x: x["votes"], reverse=True)


print(f"The winner is {candidates[0]['name']} with {candidates[0]['votes']} votes.")
print("Results:")
for candidate in candidates:
    print(f"{candidate['name']}: {candidate['votes']} votes")