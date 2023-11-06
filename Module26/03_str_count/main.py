import os
import re

def count_non_empty_lines(file_path):
    """
    Генератор вычисляет кол-во строк в файле, игнорируя пустые строки и строки комментариев.

    :param file_path: Путь к файлу.
    :yield: Кол-во непустых строк в файле.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        non_empty_lines = 0

        for line in lines:
            if not re.match(r'^\s*#|^\s*$', line):
                non_empty_lines += 1

        yield non_empty_lines

def process_python_files(directory):
    """
    Генератор обрабатывает все py файлы в указанной директории.

    :param directory: Путь к директории.
    :yield: Количество непустых строк в каждом py файле.
    """
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                yield from count_non_empty_lines(file_path)

if __name__ == "__main__":
    directory = ""
    for count in process_python_files(directory):
        print(f"Файл содержит {count} непустых строк.")
