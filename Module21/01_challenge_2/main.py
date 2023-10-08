def recursive(num):
    if num < 1:
        return
    recursive(num - 1)
    print(num)

num = int(input("Введите число: "))
if isinstance(num, int):
    recursive(num)
else:
    print("Пожалуйста, введите целое число.")





