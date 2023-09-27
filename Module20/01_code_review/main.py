students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

stud = [(student_id, student['age']) for student_id, student in students.items()]
print("Список пар 'ID студента — возраст':", stud)

interests = set()
surname_length = sum(len(student['surname']) for student in students.values())
for student in students.values():
    interests.update(student['interests'])

print("Полный список интересов всех студентов:", interests)
print("Общая длина всех фамилий студентов:", surname_length)
