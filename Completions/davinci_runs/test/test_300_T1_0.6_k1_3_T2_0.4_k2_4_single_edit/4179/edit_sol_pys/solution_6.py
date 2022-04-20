N, M, C = map(int, input().split())
B = list(map(int, input().split()))  # BにB1,B2,B3,B4,B5が入る
count = 0
for _ in range(N):
    A = list(map(int, input().split()))  # AにA1,A2,A3,A4,A5が入る
    result = 0
    for i in range(M):
        result += A[i] * B[i]
    result += C
    if result > 0:
        count += 1
print(count)
