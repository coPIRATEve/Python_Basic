def count_unique_characters(s):
    unique_count = len(set(filter(lambda x: x.isalpha(), map(lambda x: x.lower(), s))))
    return unique_count

message = "Скорей бы зима кончилась"
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)

