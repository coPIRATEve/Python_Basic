class Property:
    def __init__(self, worth):
        self._worth = worth

    def get_worth(self):
        return self._worth

    def set_worth(self, value):
        if value >= 0:
            self._worth = value
        else:
            print("Значение стоимости должно быть неотрицательным.")

    worth = property(get_worth, set_worth)

    def calculate_tax(self):
        return 0  # Базовый класс не имеет налога

class Apartment(Property):
    def calculate_tax(self):
        return self.worth / 1000

class Car(Property):
    def calculate_tax(self):
        return self.worth / 200

class CountryHouse(Property):
    def calculate_tax(self):
        return self.worth / 500

def main():
    money = float(input("Введите количество ваших денег: "))
    property_type = input("Введите тип имущества (Apartment, Car, CountryHouse): ")
    property_worth = float(input("Введите стоимость имущества: "))

    if property_type == "Apartment":
        property_obj = Apartment(property_worth)
    elif property_type == "Car":
        property_obj = Car(property_worth)
    elif property_type == "CountryHouse":
        property_obj = CountryHouse(property_worth)
    else:
        print("Неверный тип имущества.")
        return

    tax = property_obj.calculate_tax()
    money -= tax

    if money >= 0:
        print(f"Налог на {property_type}: {tax}")
        print(f"У вас осталось {money} денег.")
    else:
        print(f"Недостаточно денег для оплаты налога.")

if __name__ == "__main__":
    main()
