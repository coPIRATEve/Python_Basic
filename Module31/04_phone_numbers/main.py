import re
def check_phone_numbers(phone_numbers):
    for index, number in enumerate(phone_numbers, start=1):
        pattern = r'^[89]\d{9}$'
        if re.match(pattern, number):
            print(f'номер {index}: всё в порядке')
        else:
            print(f'номер {index}: не подходит')
phone_list = ['9999999999', '999999-999', '99999x9999']
check_phone_numbers(phone_list)

