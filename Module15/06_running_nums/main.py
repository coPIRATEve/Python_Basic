N = int(input("Кол-во элементов: "))
start_list = []
finish_list = []

for _ in range(N):
    element = input("Введите элемент списка:")
    start_list.append(element)

K = int(input("Сдвиг: "))
start_list.insert(K-1, start_list.pop())

print(start_list)

