def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def crypto(iterable):
    return [element for index, element in enumerate(iterable) if is_prime(index)]

number = input("Ведите числа через запятую: ")
numbers = number.split(', ')
numbers_list = []
for num_str in numbers:
    num = int(num_str)
    numbers_list.append(num)
word = input("Введите вашу фразу: ")
print("Ваш ввод чисел: ", crypto(numbers_list))
print("Ваш ввод фразы: ", crypto(word))
print("Пример вывода чисел: ", crypto([33, 17, 18, 16, 19, 20, 16, 12, 6, 15]))
print("Пример вывода фразы: ", crypto('Он просто кен, его работа - пляж!'))

