def generate_odd_numbers(last_num):
    odd_numbers = []
    for _ in range(1, last_num + 1, 2):
        odd_numbers.append(_)
    return odd_numbers

last_num = int(input("Введите целое число N: "))
odd_numbers_list = generate_odd_numbers(last_num)
print("Список нечетных чисел:", odd_numbers_list)

