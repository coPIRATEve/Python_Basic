rows = 4
columns = 3
starting_value = 1
difference = 4

two_dimensional_list = [
    [starting_value + j * difference for j in range(columns)]
    for starting_value in range(starting_value, starting_value + rows)
]

print(two_dimensional_list)


