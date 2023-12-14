from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

powered_floats = list(map(lambda x: round(x ** 3, 3), floats))
filtered_names = list(filter(lambda x: len(x) >= 5, names))
product_of_numbers = lambda x: x if not x else x[0] * product_of_numbers(x[1:])
result_numbers = product_of_numbers(numbers)

print("Powered Floats:", powered_floats)
print("Filtered Names:", filtered_names)
print("Product of Numbers:", result_numbers)
