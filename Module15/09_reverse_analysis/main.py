input_num = input("Введите список чисел через пробел: ")
split_numbers = input_num.split()

numbers = [int(x) for x in split_numbers]

print("Список чисел:", numbers)

for num in reversed(numbers):
    if num % 2 == 0:
        print(num)
