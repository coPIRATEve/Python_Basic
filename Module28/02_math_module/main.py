class MyMath:
    PI = 3.141592653589793

    @staticmethod
    def circle_len(radius):
        """длина окружности."""
        return 2 * MyMath.PI * radius

    @staticmethod
    def circle_sq(radius):
        """площадь окружности."""
        return MyMath.PI * radius ** 2

    @classmethod
    def cube_volume(cls, side_length):
        """объём куба."""
        return side_length ** 3

    @staticmethod
    def sphere_surface_area(radius):
        """площадь поверхности сферы."""
        return 4 * MyMath.PI * radius ** 2

    @classmethod
    def cube_surface_area(cls, side_length):
        """площадь поверхности куба."""
        return 6 * side_length ** 2


radius_value = float(input("Введите радиус: "))
side_length_value = float(input("Введите длину стороны куба: "))

res_1 = MyMath.circle_len(radius=radius_value)
res_2 = MyMath.circle_sq(radius=radius_value)
res_3 = MyMath.cube_volume(side_length=side_length_value)
res_4 = MyMath.sphere_surface_area(radius=radius_value)
res_5 = MyMath.cube_surface_area(side_length=side_length_value)

print(res_1)
print(res_2)
print(res_3)
print(res_4)
print(res_5)

