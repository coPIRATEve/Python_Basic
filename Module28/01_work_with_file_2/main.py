import os

class File:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise ValueError("Название файла должно быть текстовым")
        self._filename = value

    @property
    def mode(self):
        return self._mode
    @mode.setter
    def mode(self, value):
        if not isinstance(value, str):
            raise ValueError("Режим должен быть текстовым")
        self._mode = value
    @classmethod
    def open(cls, filename, mode='r'):
        instance = cls(filename, mode)
        return instance.__enter__()
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            self.file = open(self.filename, 'w')
        finally:
            return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return True

if __name__ == "__main__":
    file_path = "example.txt"
    with open(file_path, mode='w', encoding='utf-8') as file:
        file.write("Пришли как-то пупа и лупа устраиваться во фронт-энд. Но в компании что-то перепутали"
                   " и лупа стал разработчиком, а пупа за лупу")
    with open(file_path, mode='r', encoding='utf-8') as file:
        content = file.read()
        print(content)