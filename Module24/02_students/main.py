class Student:
    def __init__(self, full_name, group_number, grades):
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

num_students = int(input("Введите количество студентов: "))

students = []

for i in range(num_students):
    while True:
        full_name = input(f"Введите ФИО студента {i + 1} (три слова через пробел): ")
        words = full_name.split()
        if len(words) == 3:
            break
        else:
            print("ФИО должно состоять из трёх слов. Повторите ввод.")

        group_number = input(f"Введите номер группы студента {i + 1}: ")
        grades = []
        for j in range(5):
            grade = int(input(f"Введите оценку {j + 1} для студента {i + 1}: "))
            grades.append(grade)

        student = Student(full_name, group_number, grades)
        students.append(student)

students.sort(key=lambda student: student.get_average_grade())

for student in students:
    print(
        f"Студент: {student.full_name}, Группа: {student.group_number}, Средний балл: {student.get_average_grade():.2f}")

