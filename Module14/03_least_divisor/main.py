def find_smallest_divisor(number):
    if number <= 1:
        raise ValueError("Ошибка! Число должно быть натуральным и отличным от 1")
    for i in range(2, number):
        if number % i == 0:
            return i
    return number

while True:
    number = int(input("Введите натуральное число больше 1 (если хотите прекратить - 0): "))
    if number == 0:
        print("Спасибо, пока")
        break
    smallest_divisor = find_smallest_divisor(number)
    print("Наименьший делитель числа", number, "отличный от 1:", smallest_divisor)
    find_smallest_divisor(number)




