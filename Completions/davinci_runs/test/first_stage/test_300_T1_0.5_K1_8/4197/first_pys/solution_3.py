

N = int(input())
A = list(map(int, input().split()))

student_number = []
for i in range(N):
    student_number.append(0)

for i in range(N):
    student_number[A[i]-1] = i+1

print(*student_number)