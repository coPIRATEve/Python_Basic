violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

N = int(input("Сколько песен выбрать? "))
selected_songs = []

for i in range(N):
    song_name = input(f"Название {i+1}-й песни: ")
    selected_songs.append(song_name)

total_duration = 0
for song_name in selected_songs:
    for song in violator_songs:
        if song[0] == song_name:
            total_duration += song[1]
            break

print("Общее время звучания песен: " , total_duration , "минуты")
