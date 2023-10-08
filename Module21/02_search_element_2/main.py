def search_element(data, tag):
    if tag in data:
        return data[tag]
    for key, value in data.items():
        if isinstance(value, dict):
            result = search_element(value, tag)
            if result:
                return result
    return None


def select_level(data):
    level = input("Введите максимальную глубину: ")
    if level in data:
        return data[level]
    print("Значение ключа: None")
    return None


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

while True:
    search_key = input("Введите искомый ключ: ")
    level = input("Хотите ввести максимальную глубину? Y/N: ")
    if level.lower() != "n":
        result = select_level(site)
    else:
        value = search_element(site, search_key)
        if value:
            print("Значение:", value)
        else:
            print("Значение ключа: None")

    answer = input("Хотите провести еще один поиск? (да/нет): ")
    if answer.lower() != "да":
        break


