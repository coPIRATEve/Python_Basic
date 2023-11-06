import os
def error_log_generator(file_path):
    with open(file_path) as file:
        for line in file:
            if 'ERROR' in line:
                yield line


def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    with open(output_file, 'w') as out_file:
        for line in error_log_generator(input_file):
            out_file.write(line)


if __name__ == '__main__':
    main()