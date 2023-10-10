with open("first_tour.txt", "r") as file:
    lines = file.readlines()

K = int(lines[0].strip())
participants = []

for line in lines[1:]:
    data = line.strip().split()
    name = f"{data[1][0]}. {data[0]}"
    score = int(data[2])
    if score > K:
        participants.append((name, score))

participants.sort(key=lambda x: x[1], reverse=True)
with open("second_tour.txt", "w") as file:
    file.write(str(len(participants)) + "\n")
    for i, (name, score) in enumerate(participants, 1):
        file.write(f"{i}) {name} {score}\n")

