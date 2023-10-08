import os
def get_dir_info(path):
    total_s = 0
    total_f = 0
    total_dir = 0
    def calculate_dir_s(dir_path):
        nonlocal total_s, total_f, total_dir
        if os.path.exists(dir_path):
            with os.scandir(dir_path) as entries:
                for entry in entries:
                    if entry.is_file():
                        total_s += entry.stat().st_size
                        total_f += 1
                    elif entry.is_dir():
                        total_dir += 1
                        calculate_dir_s(entry.path)

    calculate_dir_s(path)
    total_s_kb = total_s / 1024

    print(f"{path}")
    print(f"Размер каталога (в Кб): {total_s_kb}")
    print(f"Количество подкаталогов: {total_dir}")
    print(f"Количество файлов: {total_f}")


path = input("Введите путь к каталогу: ")
get_dir_info(path)
