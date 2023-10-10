def calculate_letter_frequency(text):
    letter_count = {}
    total_letters = 0
    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
            total_letters += 1

    return letter_count, total_letters
def write_analysis_results(letter_count, total_letters, output_file):
    sorted_letters = sorted(letter_count.keys())
    sorted_letters.sort(key=lambda x: letter_count[x] / total_letters, reverse=True)
    file = open(output_file, 'w')
    for letter in sorted_letters:
        frequency = letter_count[letter] / total_letters
        file.write(f"{letter} {frequency:.3f}\n")
    file.close()

text_file = open('text.txt', 'r')
text = text_file.read()
text_file.close()

letter_count, total_letters = calculate_letter_frequency(text)
write_analysis_results(letter_count, total_letters, 'analysis.txt')
