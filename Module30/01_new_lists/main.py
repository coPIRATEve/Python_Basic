from functools import reduce
from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

powered_floats = list(map(lambda x: round(x ** 3, 3), floats))
filtered_names = list(filter(lambda x: len(x) >= 5, names))
result_numbers = reduce(lambda num1, num2: num1 * num2, numbers)

print(" из списка floats возводится в третью степень и округляется до трёх знаков после запятой:", powered_floats)
print("Из списка names берутся только те имена, в которых есть минимум пять бук:", filtered_names)
print("Из списка numbers берётся произведение всех чисел:", result_numbers)
