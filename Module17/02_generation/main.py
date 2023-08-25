N = int(input("Введите длину списка: "))

result = [("1" if number % 2 == 0 else number % 5)
          for number in range(N)]
print(result)
