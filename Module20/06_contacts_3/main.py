contacts = {}

while True:
    print("Введите номер действия:")
    print("1. Добавить контакт")
    print("2. Найти человека")
    action = input()

    if action == "1":
        full_name = input("Введите имя и фамилию нового контакта (через пробел): ").split()
        phone_number = input("Введите номер телефона: ")
        last_name = full_name[1].lower()
        if tuple(full_name) in contacts:
            print("Такой человек уже есть в контактах")
        else:
            contacts[tuple(full_name)] = phone_number
            print("Текущий словарь контактов:", contacts)

    elif action == "2":
        search_last_name = input("Введите фамилию для поиска: ").lower()
        found_contacts = [(name, phone) for name, phone in contacts.items() if name[1].lower() == search_last_name]
        if found_contacts:
            print("Найденные контакты:")
            for name, phone in found_contacts:
                print(f"{name[0]} {name[1]} {phone}")
        else:
            print("Контакты с такой фамилией не найдены")

    else:
        print("Попробуй еще раз")
