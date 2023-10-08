def custom_sum(*args):
    total = 0
    for arg in args:
        if isinstance(arg, list):
            total += custom_sum(*arg)
        elif isinstance(arg, int):
            total += arg
    return total

