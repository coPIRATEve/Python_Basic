def palindrome(s):
    s = s.replace(" ", "").lower()
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return "Можно сделать палиндромом"
    else:
        return "Нельзя сделать палиндромом"


user_input = input("Введите строку: ")
result = palindrome(user_input)
print(result)

