main_list = [1, 5, 3]
first_side = [1, 5, 1, 5]
second_side = [1, 3, 1, 5, 3, 3]

main_list.extend(first_side)
num_count1 = main_list.count(5)
main_list = [num for num in main_list if num != 5]

main_list.extend(second_side)
num_count2 = main_list.count(3)

print("итоговый список:", main_list)
print("кол-во пятёрок:", num_count1, "кол-во троек:", num_count2)
