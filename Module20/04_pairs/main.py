import random

original_list = [random.randint(0, 100) for _ in range(10)]
new_list = [(original_list[i], original_list[i + 1]) for i in range(0, len(original_list), 2)]

print("Оригинальный список:", original_list)
print("Новый список:", new_list)

