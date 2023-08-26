def find_longest_word(input_string):
    words = input_string.split()
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word, len(longest_word)

input_string = input("Введите строку с пробелами: ")
longest_word, length = find_longest_word(input_string)
print("Самое длинное слово: {longest_word}. Длина слова: {length}!".format(longest_word=longest_word, length=length))

