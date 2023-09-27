array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Решение без множеств
common_elements = []
for element in array_1:
    if element in array_2 and element in array_3:
        common_elements.append(element)
# Решение с использованием множеств
set_1 = set(array_1)
set_2 = set(array_2)
set_3 = set(array_3)
common_elements_with_sets = list(set_1.intersection(set_2, set_3))
# Решение без множеств
not_in_array_2_and_3 = []
for element in array_1:
    if element not in array_2 and element not in array_3:
        not_in_array_2_and_3.append(element)
# Решение с использованием множеств
not_in_set_2_and_3 = list(set_1.difference(set_2, set_3))
print("Задача 1:")
print("Решение без множеств:", common_elements)
print("Решение с множествами:", common_elements_with_sets)
print("\nЗадача 2:")
print("Решение без множеств:", not_in_array_2_and_3)
print("Решение с множествами:", not_in_set_2_and_3)
