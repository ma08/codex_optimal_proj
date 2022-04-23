

# S = sum(Ai) + x # S is sum of current scores of students
# x = M * N - S # x is required score

N, K, M = map(int, input().split()) # N is the number of students, K is the max score, M is the average score
A = list(map(int, input().split())) # A is the list of current scores of students

S = sum(A)
x = M * N - S

if x < 0:
    print(-1)
elif x > K:
    print(-1)
else:
    print(x)
