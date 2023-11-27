import functools
import logging
from datetime import datetime

logging.basicConfig(filename='function_errors.log', level=logging.ERROR)

def logging_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(f"Вызвана функция: {func.__name__}")
            print(f"Документация: {func.__doc__}")
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            error_message = f"{func.__name__} - {datetime.now()} - {str(e)}"
            logging.error(error_message)
            print(f"Ошибка в функции {func.__name__}: {str(e)}")
            pass

    return wrapper

@logging_decorator
def sum(num1, num2):
    """
    Эта функция складывает числа.
    """
    return num1 + num2

@logging_decorator
def square_root(x):
    """
    Эта функция вычисляет квадратный корень из x.
    """
    if x < 0:
        raise ValueError("Нельзя извлекать квадратный корень из отрицательного числа.")
    return x ** 0.5

sum1 = sum(10, 2)
sum2 = sum(10, 0)
result1 = square_root(25)
result2 = square_root(-1)
