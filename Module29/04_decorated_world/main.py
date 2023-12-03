from functools import wraps
from typing import Callable

def decorator_with_args_for_any_decorator(*args, **kwargs):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*func_args, **func_kwargs):
            print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
            result = func(*func_args, **func_kwargs)
            return result
        return wrapper
    return decorator

@decorator_with_args_for_any_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет, ", text, num)

decorated_function("Юзер", 101)

