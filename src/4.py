from functools import reduce

n = int(input())
students = {}
for _ in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    students[name] = marks

student_name = input()

# Реализуйте поиск среднего балла для указанного студента
# Выведите результат с точностью до 2 знаков после запятой

print(
    f"{
        (
            reduce(lambda x, y: x + y, students[student_name])
            / len(students[student_name])
        ):.2f}"
)
