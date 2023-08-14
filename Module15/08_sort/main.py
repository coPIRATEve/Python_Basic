def bubble(arr): #использовала метод пузырька, как в плюсах, покумекала, вроде работает
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input("Введите количество чисел: "))
numbers = []
for i in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)

bubble(numbers)

print("Отсортированный список:")
for num in numbers:
    print(num, end=" ")
    print()
