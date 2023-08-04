def is_point_inside_circle(x, y, r):
    distance_squared = x**2 + y**2
    if distance_squared <= r**2:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")


x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
r = float(input("Введите радиус круга: "))

is_point_inside_circle(x, y, r)

