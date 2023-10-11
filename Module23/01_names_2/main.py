list_of_names = ['Василий', 'Николай', 'Надежда', 'Никита',
                 'Ян', 'Ольга', 'Евгения', 'Кристина']


def fun_err_and_char_count(list_of_names, file_name, errors_file):
    total_symbols = 0
    line_count = 0
    try:
        with open(file_name, 'w+', encoding='utf-8') as file:
            file.write('\n'.join(list_of_names))
            file.seek(0)
            print(f'Содержимое файла people.txt: \n{file.read()}')
            file.seek(0)
            print('\nОтвет в консоли:')
            for line in file:
                try:
                    line_count += 1
                    total_symbols += len(line.strip())
                    if len(line.strip()) < 3:
                        raise ValueError
                except ValueError:
                    print(f'Ошибка: менее трёх символов в строке {line_count}.')
    except Exception as err:
        with open(errors_file, 'w', encoding='utf-8') as new_file:
            new_file.write(str(err))
    finally:
        return total_symbols


file_name = 'people.txt'
errors_file = 'errors.log'
total_number_of_characters = fun_err_and_char_count(list_of_names, file_name, errors_file)
print(f'Общее количество символов: {total_number_of_characters}.')
