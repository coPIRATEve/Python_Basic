def create_synonym_dictionary():
    synonym_dict = {}
    n = int(input("Введите количество пар слов: "))

    for i in range(n):
        pair = input(f"Введите {i + 1}-ю пару слов через знак ' — ': ")
        words = pair.split(" — ")
        if len(words) != 2:
            print("Ошибка: Неверный формат пары слов. Попробуйте еще раз.")
            continue
        word1, word2 = words
        synonym_dict[word1.lower()] = word2
        synonym_dict[word2.lower()] = word1

    return synonym_dict

def find_synonym(synonym_dict, word):
    word_lower = word.lower()
    if word_lower in synonym_dict:
        return synonym_dict[word_lower]
    else:
        return None

synonym_dict = create_synonym_dictionary()

while True:
    search_word = input("Введите слово: ")
    synonym = find_synonym(synonym_dict, search_word)
    if synonym:
        print(f"Синоним: {synonym}")
    else:
        print("Такого слова в словаре нет.")
