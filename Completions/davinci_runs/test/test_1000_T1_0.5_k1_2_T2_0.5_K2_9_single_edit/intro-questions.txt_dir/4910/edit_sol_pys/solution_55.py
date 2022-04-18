

from collections import defaultdict

n = int(input("Enter the number of students: "))
students = [input("Enter student name: ") for _ in range(n)]

marks = defaultdict(int)
for student in students:
    marks[student] += 1

max_count = max(marks.values())
best_students = [student for student, count in marks.items() if count == max_count]
best_students.sort()

for student in best_students:
    print(student)
