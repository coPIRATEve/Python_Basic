import math
def get_sage_sqrt(number):
    try:
        if number < 0:
            raise ValueError("Отрицательное число не имеет действительного квадратного корня")
        result = math.sqrt(number)
        return result
    except ValueError as ve:
        return f"Ошибка: {ve}"
    except Exception as exc:
        return f"Произошла неожиданная ошибка: {exc}"

numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")