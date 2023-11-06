import os
def gen_files_path(directory='/', target_directory=None):
    file_paths = []

    for root, _, files in os.walk(directory):
        if target_directory is None or os.path.abspath(root) == os.path.abspath(target_directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    return file_paths

target_directory = 'C:\\'
file_paths = gen_files_path(target_directory=target_directory)

for file_path in file_paths:
    print(file_path)
