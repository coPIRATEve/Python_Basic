def memoize(func):
    cash = {}
    def wrapper(*args):
        if args not in cash:
            cash[args] = func(*args)
        return cash[args]
    return wrapper
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))
print(fibonacci(10))
