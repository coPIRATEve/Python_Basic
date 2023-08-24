alphabet = ['АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' , 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
letter = input('Введите сообщение: ')
k = int(input('Введите сдвиг: '))
cezar_letter = ''
for ch in letter:
  for r in alphabet:
    if (p := r.find(ch)) >= 0:
      ch = r[(p + k) % len(r)]
      break
  cezar_letter += ch
print('Зашифрованное сообщение:', cezar_letter)