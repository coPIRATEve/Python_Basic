import random
def generate_participants_list():
    participants_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
    return participants_list

team1 = generate_participants_list()
team2 = generate_participants_list()

winners = [max(participant1, participant2) for participant1, participant2 in zip(team1, team2)]

print("Первая команда:", team1)
print("Вторая команда:", team2)
print("Победители тура:", winners)
