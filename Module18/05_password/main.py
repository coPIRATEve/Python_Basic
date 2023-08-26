print('Внимание, придумайте пароль! Этот пароль должен состоять минимум из восьми символов, '
      '\nв нём должны быть хотя бы одна большая буква и хотя бы три цифры: ')
while True:
    password = input()
    if len(password) < 8:
        print("Пароль слишком короткий. Требуется минимум 8 символов.")
    elif not any(letter.isupper() for letter in password):
        print("Пароль должен содержать хотя бы одну большую букву.")
    elif sum(letter.isdigit() for letter in password) < 3:
        print("Пароль должен содержать хотя бы три цифры.")
    else:
        print("Пароль надёжный. Регистрация завершена.")
        break
