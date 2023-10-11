import random
def write_to_file(number, filename):
    with open(filename, 'a') as file:
        file.write(str(number) + '\n')


total = 0
filename = 'out_file.txt'

while total < 777:
    try:
        user_input = float(input("Введите число: "))
        total += user_input
        write_to_file(user_input, filename)
        if random.randint(1, 13) == 1:
            raise Exception("Вас постигла неудача!")
    except ValueError:
        print("Неверный формат числа. Пожалуйста, введите число снова.")

print("Вы успешно выполнили условие для выхода из порочного цикла!")
