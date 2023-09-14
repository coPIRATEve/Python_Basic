def invert_frequency_dict(text):
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    inverted_dict = {}

    for char, num in dict.items():
        if num in inverted_dict:
            inverted_dict[num].append(char)
        else:
            inverted_dict[num] = [char]

    print("Оригинальный словарь частот:")
    for char, num in sorted(dict.items()):
        print(f"{char} : {num}")

    print("\nИнвертированный словарь частот:")
    for num, chars in sorted(inverted_dict.items()):
        print(f"{num} : {chars}")

text = input("Введите текст: ")
invert_frequency_dict(text)

