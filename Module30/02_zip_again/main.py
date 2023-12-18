letters = ['с', 'е', 'с', 'с', 'и', 'я']
numbers = [4, 5, 6, 8, 10]

results = list(map(lambda x, y: (x, y), letters, numbers[:len(letters)]))
print(results)

