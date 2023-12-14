from collections import Counter

def can_be_poly(s: str) -> bool:
    """
    Проверяет, можно ли из строки получить палиндром.

    :param s: Входная строка
    :type s: str
    :return: True, если можно получить палиндром, иначе False
    :rtype: bool
    """

    char_count = Counter(s)

    is_even = lambda x: x % 2 == 0

    odd_count = sum(map(lambda x: not is_even(x), char_count.values()))

    return odd_count <= 1

print(can_be_poly('кошка'))
print(can_be_poly('шалаш'))

