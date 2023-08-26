
def count_uppercase_lowercase(text):
    uppercase_count = 0
    lowercase_count = 0

    for _ in text:
        if _.isupper():
            uppercase_count += 1
        elif _.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_counе


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
