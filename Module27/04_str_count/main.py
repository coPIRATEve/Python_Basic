import functools

def counter(func):
    """Декоратор, который подсчитывает и печатает количество вызовов оформленной функции."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Функцмя {func.__name__} была вызвана {wrapper.calls} раз.")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@counter
def example_function():
    """Пример функции."""
    print("Выполнение примерной функции.")
example_function()


