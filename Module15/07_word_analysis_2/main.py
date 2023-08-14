while True:
    word = input('Введите слово (Чтобы прекратить - конец): ')
    if word == 'конец':
        print('конец работы')
        break

    word_list = list(word)
    reversed_word_list = word_list.copy()
    reversed_word_list.reverse()

    if word_list == reversed_word_list:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")
