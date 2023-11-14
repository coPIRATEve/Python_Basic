#класс итератор
class SquaresIterator:
    def __init__(self, N):
        self.N = N
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.N:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

#Функция-генератор
def generate_squares(N):
    current = 1
    while current <= N:
        yield current ** 2
        current += 1

#Генераторное выражение
n = int(input("Введите число N: "))
squares = (x ** 2 for x in range(1, n + 1))
print("Вывод генераторного выражения: ")
for square in squares:
    print(square)

squares = SquaresIterator(n)
print("Вывод класса-итератора: ")
for square in squares:
    print(square)

squares = generate_squares(n)
print("Вывод функции-генератора")
for square in squares:
    print(square)
