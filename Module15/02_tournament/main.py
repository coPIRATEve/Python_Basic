participants = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
print("Дан список имён участников: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар.")

firstday_participants = []
for i in range(0, len(participants), 2):
    firstday_participants.append(participants[i])

print("На первый день соревнований попадут:", ", ".join(firstday_participants))


