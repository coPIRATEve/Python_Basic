people_num = int(input("Введите кол-во людей: "))
people_list = list(range(1, people_num + 1))

k = int(input("Какое число в считалке? "))

for i in range(k - people_num + 1):
    print("Текущий круг людей: ", people_list)
    if k > people_num:
        k -= people_num

    if abs(k) <= people_num:
        del people_list[k - 1]
    k -= 2
print("Текущий круг людей: ", people_list)
last_remaining_number = people_list[0]
print("Последнее оставшееся число:", last_remaining_number)
