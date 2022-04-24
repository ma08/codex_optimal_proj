
#n = int(input())
#students = list(map(int, input().split()))
#
#max_skill = max(students)
#
#min_n_problems = 0
#for i in range(1, max_skill+1):
#    n_students = 0
#    for student in students:
#        if student >= i:
#            n_students += 1
#    if n_students % 2 == 1:
#        min_n_problems += 1
#
#print(min_n_problems)

n = int(input())
students = list(map(int, input().split()))
students.sort()
print(students[n//2])
