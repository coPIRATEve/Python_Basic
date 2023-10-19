def validate_registration(line):
    fields = line.split()

    if len(fields) != 3:
        raise IndexError("Не хватает полей")

    name, email, age = fields

    if not name.isalpha():
        raise NameError("Поле 'Имя' содержит не только буквы")

    if not ('@' in email and '.' in email):
        raise SyntaxError("Поле 'Имейл' не содержит '@' и '.'")

    age = int(age)
    if age < 10 or age > 99:
        raise ValueError("Поле 'Возраст' не является числом от 10 до 99")

    return True


with open('registrations.txt', 'r', encoding='utf-8') as input_file, \
        open('registrations_good.log', 'w', encoding='utf-8') as good_file, open(
        'registrations_bad.log', 'w', encoding='utf-8') as bad_file:
    for line in input_file:
        line = line.strip()
        try:
            if validate_registration(line):
                good_file.write(line + '\n')
        except (IndexError, NameError, SyntaxError, ValueError) as e:
            bad_file.write(f"{line} - {e}\n")

