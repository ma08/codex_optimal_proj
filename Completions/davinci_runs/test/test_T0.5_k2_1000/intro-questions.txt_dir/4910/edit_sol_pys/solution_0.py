from collections import defaultdict

n = int(input())  # number of students
students = [input() for _ in range(n)]

grades = defaultdict(int)
for student in students:
    grades[student] += 1

max_count = max(grades.values())
best_students = [student for student, count in grades.items() if count == max_count]
best_students.sort()

for student in best_students:
    print(student)
