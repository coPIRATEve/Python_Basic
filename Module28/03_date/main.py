class Date:
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    def __str__(self):
        return f"День: {self.day}\tМесяц: {self.month}\tГод: {self.year}"

    @classmethod
    def is_date_valid(cls, date_str):
        try:
            day, month, year = map(int, date_str.split('-'))
            if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100:
                return True
            else:
                return False
        except ValueError:
            return False

    @classmethod
    def from_string(cls, date_str):
        if cls.is_date_valid(date_str):
            day, month, year = map(int, date_str.split('-'))
            return cls(day, month, year)
        else:
            raise ValueError("Некорректная дата")

# Пример использования:
date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
