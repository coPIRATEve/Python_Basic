def cyclic_shift_check(str1, str2):
    if len(str1) != len(str2):
        print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
        return

    for i in range(len(str1)):
        if str1 == str2[i:] + str2[:i]:
            print("Первая строка получается из второй со сдвигом", i)
            return

    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")

first_string = input("Первая строка: ")
second_string = input("Вторая строка: ")
cyclic_shift_check(first_string, second_string)
