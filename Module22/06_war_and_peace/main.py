import zipfile
import collections

with zipfile.ZipFile("D:\Python_Basic\Module22\06_war_and_peace\voyna-i-mir.zip", "r") as archive:
    with archive.open("voina-i-mir.txt", "r") as file:
        text = file.read().decode("utf-8")

text = text.lower()
letter_counts = collections.Counter(text)
sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")
