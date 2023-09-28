def custom_zip(zip1, zip2):
    zipped = []
    min_length = min(len(zip1), len(zip2))
    for i in range(min_length):
        zipped.append((zip1[i], zip2[i]))
    return zipped

number = input("Введите числа через запятую: ")
numbers = number.split(', ')
numbers_list = []
for num_str in numbers:
    num = int(num_str)
    numbers_list.append(num)
word = input("Введите ваше слово: ")

zipped_list = custom_zip(numbers_list, word)

print("Список пар:")
for pair in zipped_list:
    print(pair)
