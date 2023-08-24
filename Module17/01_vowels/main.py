def finder(text):
    vowels = 'аеёиоуыэюя'
    vowel_list = [char for char in text.lower() if char in vowels]
    return vowel_list

user_input = input("Введите текст на русском языке: ")
vowels_list = finder(user_input)

print("Список гласных букв:", vowels_list)
print("Длина списка:", len(vowels_list))

