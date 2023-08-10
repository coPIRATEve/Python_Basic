films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня']

num_films = int(input("Сколько фильмов хотите добавить? "))

favorite_films = []

for _ in range(num_films):
    film_name = input("Введите название фильма: ")
    if film_name in films:
        favorite_films.append(film_name)
    else:
        print("Ошибка: фильма" , film_name, "у нас нет :(")

print("Ваш список любимых фильмов:", ', '.join(favorite_films))

