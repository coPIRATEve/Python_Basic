violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num_songs = int(input("Введите количество песен: "))
selected_songs = []

for i in range(num_songs):
    song_name = input(f"Введите название {i + 1}-й песни: ")
    if song_name in violator_songs:
        selected_songs.append(violator_songs[song_name])
    else:
        print(f"Песня с названием '{song_name}' не найдена в списке.")

total_time = sum(selected_songs)
print(f"Общее время звучания выбранных песен: {total_time:.2f} минут")
