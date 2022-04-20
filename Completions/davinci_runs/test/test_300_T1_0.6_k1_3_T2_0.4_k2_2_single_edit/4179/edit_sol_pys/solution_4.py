
N, M, C = map(int, input().split())
B = list(map(int, input().split()))
count = 0
for _ in range(N):
    A = list(map(int, input().split()))
    result = C
    for i in range(M):
        result += A[i] * B[i]
    if result > 0:
        count += 1
print(count)
