
N, M, C = map(int, input().split())
B = list(map(int, input().split()))
count = 0
for _ in range(N):
    A = list(map(int, input().split()))
    result = 0
    for i, j in zip(A, B):
        result += i * j
    result += C
    if result > 0:
        count += 1
print(count)
