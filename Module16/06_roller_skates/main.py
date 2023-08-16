num_skates = int(input("Кол-во коньков: "))
skate_sizes = []

for i in range(num_skates):
    size = int(input("Размер", i + 1,"-й пары: "))
    skate_sizes.append(size)

num_people = int(input("Кол-во людей: "))
people_sizes = []

for i in range(num_people):
    size = int(input("Размер", i + 1,"-го человека: "))
    people_sizes.append(size)

num_fitted = 0

for person_size in people_sizes:
    for skate_size in skate_sizes:
        if person_size == skate_size:
            num_fitted += 1
            skate_sizes.remove(skate_size)
            break

print("Наибольшее кол-во людей, которые могут взять ролики:", num_fitted)

