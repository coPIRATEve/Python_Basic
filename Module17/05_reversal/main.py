def reverse_between_h(s):
    first_h = s.index('h')
    last_h = s.rindex('h')
    substring_between_h = s[first_h+1:last_h][::-1]
    return substring_between_h

input_string = input("Введите строку: ")
print("Развёрнутая последовательность между первым и последним h:", reverse_between_h(input_string))

