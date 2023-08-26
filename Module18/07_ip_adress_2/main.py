def is_valid_ip(part):
    parts = part.split('.')
    if len(parts) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        return False
    for part in parts:
        if not part.isdigit():
            print('a4 — это не целое число..')
            return False
        num = int(part)
        if num < 0 or num > 255:
            print('340 превышает 255.')
            return False
    return True


ip_input = input("Введите IP: ")
if is_valid_ip(ip_input):
    print("IP-адрес корректен.")
else:
    print("Попробуйте снова.")

