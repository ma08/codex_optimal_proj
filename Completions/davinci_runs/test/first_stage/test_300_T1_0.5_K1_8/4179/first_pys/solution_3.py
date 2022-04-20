

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

count = 0
for i in range(N):
    result = 0
    for j in range(M):
        result += A[i][j] * B[j]
    result += C
    if result > 0:
        count += 1
print(count)