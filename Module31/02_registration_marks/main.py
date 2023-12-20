import re
def find_car_taxi_numbers(text):
    private_car_pattern = re.compile(r'([АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3})')
    taxi_pattern = re.compile(r'([АВЕКМНОРСТУХ]{2}\d{3}\d{2,3})')
    private_car_numbers = private_car_pattern.findall(text)
    taxi_numbers = taxi_pattern.findall(text)

    return private_car_numbers, taxi_numbers

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
private_cars, taxis = find_car_taxi_numbers(text)

print(f"Список номеров частных автомобилей: {private_cars}")
print(f"Список номеров такси: {taxis}")
