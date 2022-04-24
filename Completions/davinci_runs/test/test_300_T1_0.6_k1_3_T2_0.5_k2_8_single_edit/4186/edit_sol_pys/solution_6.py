


n = int(input())
students = [int(input()) for _ in range(n)]

max_skill = max(students)

min_n_problems = 0
for i in range(1, max_skill+1):
    n_students = sum([1 for student in students if student >= i])
    if n_students % 2 == 1:
        min_n_problems += 1

print(min_n_problems)
