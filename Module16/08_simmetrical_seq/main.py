def make_symmetric_sequence(sequence):
    n = len(sequence)
    additions = []

    for i in range(n):
        if sequence[i:] == sequence[i:][::-1]:
            additions = sequence[:i][::-1]
            break

    return additions

N = int(input("Кол-во чисел: "))

sequence = []
for _ in range(N):
    num = int(input("Число: "))
    sequence.append(num)

additions = make_symmetric_sequence(sequence)

print("Последовательность:", sequence + additions)
print("Нужно приписать чисел:", len(additions))
print("Сами числа:", additions)

