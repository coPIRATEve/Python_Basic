def summ_N(Number):
    sum = 0
    need_num = Number
    while Number > 0:
        sum += Number % 10
        Number //= 10
    print('Число', need_num, 'имеет максимальную сумму цифр:', sum)
    return sum

def amount_N(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    print('Количество цифр:', count)
    return count

Number = int(input('Введите число, чтобы в ответ вывело разность суммы его чисел и их количества: '))
sum_result = summ_N(Number)
count_result = amount_N(Number)

print('Число', Number, 'Количество цифр:', count_result)
print('Число', Number, 'имеет максимальную сумму цифр:', sum_result)
print("Разность суммы и количества цифр:", sum_result - count_result)
