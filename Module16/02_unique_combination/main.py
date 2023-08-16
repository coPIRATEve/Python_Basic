def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            merged.append(list2[j])
            j += 1
        else:
            merged.append(list1[i])
            i += 1
            j += 1

    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

list1 = []
list2 = []
list1_amt = int(input("Сколько чисел в 1 списке? "))
for i in range(list1_amt):
    num = int(input(f"{i + 1} число в списке: "))
    list1.append(num)

list2_amt = int(input("Сколько чисел в 2 списке? "))
for i in range(list2_amt):
    num = int(input(f"{i + 1} число в списке: "))
    list2.append(num)

merged = merge_sorted_lists(list1, list2)
print(merged)
